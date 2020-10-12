from abc import ABC, abstractmethod


class Request:
    """Request model."""

    def __init__(self, url, user):
        self.url = url
        self.user = user


class RequestHandler(ABC):
    """Request handler interface."""

    @abstractmethod
    def handle(self, request):
        raise NotImplementedError


class TemplateHandlerMixin(RequestHandler):
    """Abstract template mixin for RequestHandler."""
    template_suffix = ".template"

    def handle(self, request):
        template_name = self.get_template_name(request.url)
        if not self.is_valid_template(template_name):
            return self.handle_invalid_template(request)
        return self.render_template(template_name)

    @abstractmethod
    def get_template_name(self, request_url):
        raise NotImplementedError

    def is_valid_template(self, template_name):
        return template_name.endswith(self.template_suffix)

    @staticmethod
    def handle_invalid_template(request):
        return f"<p>Invalid entry for {request.url}</p>"

    @abstractmethod
    def render_template(self, template_name):
        raise NotImplementedError


class AuthHandlerMixin(RequestHandler):
    """Abstract auth mixin for RequestHandler."""

    def handle(self, request):
        if not self.is_valid_user(request.user):
            return self.handle_invalid_user(request)
        return super().handle(request)

    @abstractmethod
    def is_valid_user(self, request_user):
        raise NotImplementedError

    @staticmethod
    def handle_invalid_user(request):
        return f"<p>Access denied for {request.url}</p>"


class TemplateFolderHandler(TemplateHandlerMixin):
    """Concrete template handler."""

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
    """Concrete auth and template handler."""

    def __init__(self, admin_users, template_dir):
        super().__init__(template_dir)
        self.admin_users = admin_users

    def is_valid_user(self, request_user):
        return request_user in self.admin_users


def main():
    # Handle requests with simple template handler
    simple_dir = {"welcome.template": "<p>Hello world</p>",
                  "about.template": "<p>About me</p>"}
    welcome_from_nobody = Request("/welcome.template", "nobody")
    about_from_nobody = Request("/about.template", "nobody")
    foo_from_nobody = Request("/foo.bar", "nobody")
    simple_handler = TemplateFolderHandler(simple_dir)
    assert simple_handler.handle(welcome_from_nobody) == "<p>Hello world</p>"
    assert simple_handler.handle(about_from_nobody) == "<p>About me</p>"
    assert simple_handler.handle(foo_from_nobody) == "<p>Invalid entry for /foo.bar</p>"

    # Handle requests with admin template handler
    admin_users = {"john", "jane"}
    admin_dir = {"fqdn.template": "<p>server.example.com</p>",
                 "salary.template": "<p>123456789.00</p>"}
    fqdn_from_john = Request("/fqdn.template", "john")
    salary_from_jane = Request("/salary.template", "jane")
    salary_from_nobody = Request("/salary.template", "nobody")
    foo_from_john = Request("/foo.bar", "john")
    admin_handler = AdminTemplateHandler(admin_users, admin_dir)
    assert admin_handler.handle(fqdn_from_john) == "<p>server.example.com</p>"
    assert admin_handler.handle(salary_from_jane) == "<p>123456789.00</p>"
    assert admin_handler.handle(salary_from_nobody) == "<p>Access denied for /salary.template</p>"
    assert admin_handler.handle(foo_from_john) == "<p>Invalid entry for /foo.bar</p>"


if __name__ == '__main__':
    main()
