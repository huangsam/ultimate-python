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
    failure_content = "<p>Not found</p>"

    def handle(self, request):
        template_name = self.get_template_name(request.url)
        if self.is_valid_template(template_name):
            return self.render_template(template_name)
        return self.failure_content

    @abstractmethod
    def get_template_name(self, request_url):
        raise NotImplementedError

    @abstractmethod
    def is_valid_template(self, template_name):
        return template_name.endswith(self.template_suffix)

    @abstractmethod
    def render_template(self, template_name):
        raise NotImplementedError


class AuthHandlerMixin(RequestHandler):
    """Abstract auth mixin for RequestHandler."""
    success_content = "<p>Something private</p>"
    failure_content = "<p>Access denied</p>"

    def handle(self, request):
        if self.is_valid_user(request.user):
            return self.success_content
        return self.failure_content

    @abstractmethod
    def is_valid_user(self, request_user):
        raise NotImplementedError


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


class AdminHandler(AuthHandlerMixin):
    """Concrete auth handler."""
    success_content = "<p>Admin stuff</p>"

    def __init__(self, admin_users):
        self.admin_users = admin_users

    def is_valid_user(self, request_user):
        return request_user in self.admin_users


def main():
    welcome_handler = TemplateFolderHandler({"welcome.template": "<p>Hello world</p>"})
    assert welcome_handler.handle(Request("/welcome.template", "nobody")) == "<p>Hello world</p>"
    assert welcome_handler.handle(Request("/foo.bar", "nobody")) == "<p>Not found</p>"

    admin_handler = AdminHandler({"john", "jane"})
    assert admin_handler.handle(Request("/admin.html", "john")) == "<p>Admin stuff</p>"
    assert admin_handler.handle(Request("/admin.html", "nobody")) == "<p>Access denied</p>"


if __name__ == '__main__':
    main()
