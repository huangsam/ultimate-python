"""
Mixins are a way to provide implementation details that simplify the work
for a developer to conform to an opaque interface specification. In this
module, we have one request handler interface and two request handler
mixins to illustrate how mixins can make our lives easier when defining
concrete classes.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Request:
    """Request data model.

    Assumes only GET requests for simplicity so there is no method
    attribute associated with this class.
    """
    url: str
    user: str


class RequestHandler(ABC):
    """Request handler interface.

    In the real world, a URL is expected to handle different kinds of HTTP
    methods. To support this, we would define a `View` class with a method
    that dispatches the request payload to the appropriate HTTP handler.
    Afterward, we would register the class to a URL router. Check out
    the source code in Django and Flask to see how that works:

    https://github.com/django/django
    https://github.com/pallets/flask
    """

    @abstractmethod
    def handle(self, request):
        """Handle incoming request."""
        raise NotImplementedError


class TemplateHandlerMixin(RequestHandler):
    """Abstract template mixin for RequestHandler.

    This is a mixin because it's an abstract class that provides a
    concrete implementation of the `handle` method. In other words, it
    adds additional structure for implementing the `handle` routine. This
    class helps if downstream developers typically implement request
    handlers that retrieve template content.
    """
    template_suffix = ".template"

    def handle(self, request):
        template_name = self.get_template_name(request.url)
        if not self.is_valid_template(template_name):
            return self.handle_invalid_template(request)
        return self.render_template(template_name)

    @abstractmethod
    def get_template_name(self, request_url):
        """Get template name."""
        raise NotImplementedError

    def is_valid_template(self, template_name):
        """Check if template name is valid."""
        return template_name.endswith(self.template_suffix)

    @staticmethod
    def handle_invalid_template(request):
        """Handle request for invalid template."""
        return f"<p>Invalid entry for {request.url}</p>"

    @abstractmethod
    def render_template(self, template_name):
        """Render contents of specified template name."""
        raise NotImplementedError


class AuthHandlerMixin(RequestHandler):
    """Abstract auth mixin for RequestHandler.

    This is another mixin class where authentication helper methods are
    defined in this abstract class and must be implemented in concrete
    classes. Notice that the `handle` method is implemented and returns
    the output of the parent's `handle` method. This means that we can
    continue to chain mixin effects as long as this mixin is to the left
    of another mixin in a concrete class MRO.
    """

    def handle(self, request):
        if not self.is_valid_user(request.user):
            return self.handle_invalid_user(request)
        return super().handle(request)

    @abstractmethod
    def is_valid_user(self, request_user):
        """Check if user is valid."""
        raise NotImplementedError

    @staticmethod
    def handle_invalid_user(request):
        """Handle request for invalid user."""
        return f"<p>Access denied for {request.url}</p>"


class TemplateFolderHandler(TemplateHandlerMixin):
    """Concrete template handler.

    This concrete class implements the abstract methods of its parent
    mixin. By extension, it has implemented everything that is needed
    for the `handle` method.
    """

    def __init__(self, template_dir):
        self.template_dir = template_dir

    def get_template_name(self, request_url):
        return request_url[1:]

    def is_valid_template(self, template_name):
        return (super().is_valid_template(template_name)
                and template_name in self.template_dir)

    def render_template(self, template_name):
        return self.template_dir[template_name]


class AdminTemplateHandler(AuthHandlerMixin, TemplateFolderHandler):
    """Concrete auth and template handler.

    This concrete class gets the benefits of the previous concrete
    class but also gets authentication for free just by implementing
    the abstract method of the authentication mixin.
    """

    def __init__(self, admin_users, template_dir):
        super().__init__(template_dir)
        self.admin_users = admin_users

    def is_valid_user(self, request_user):
        return request_user in self.admin_users


def main():
    # Handle requests with simple template handler
    simple_dir = {"welcome.template": "<p>Hello world</p>",
                  "about.template": "<p>About me</p>"}
    simple_handler = TemplateFolderHandler(simple_dir)
    welcome_from_nobody = Request("/welcome.template", "nobody")
    about_from_nobody = Request("/about.template", "nobody")
    foo_from_nobody = Request("/foo.bar", "nobody")
    assert simple_handler.handle(welcome_from_nobody) == "<p>Hello world</p>"
    assert simple_handler.handle(about_from_nobody) == "<p>About me</p>"
    assert simple_handler.handle(foo_from_nobody) == "<p>Invalid entry for /foo.bar</p>"

    # Handle requests with admin template handler
    admin_users = {"john", "jane"}
    admin_dir = {"fqdn.template": "<p>server.example.com</p>",
                 "salary.template": "<p>123456789.00</p>"}
    admin_handler = AdminTemplateHandler(admin_users, admin_dir)
    fqdn_from_john = Request("/fqdn.template", "john")
    salary_from_jane = Request("/salary.template", "jane")
    salary_from_nobody = Request("/salary.template", "nobody")
    foo_from_john = Request("/foo.bar", "john")
    assert admin_handler.handle(fqdn_from_john) == "<p>server.example.com</p>"
    assert admin_handler.handle(salary_from_jane) == "<p>123456789.00</p>"
    assert admin_handler.handle(salary_from_nobody) == "<p>Access denied for /salary.template</p>"
    assert admin_handler.handle(foo_from_john) == "<p>Invalid entry for /foo.bar</p>"


if __name__ == "__main__":
    main()
