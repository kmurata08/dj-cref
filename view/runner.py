from abc import abstractmethod, ABCMeta


GENERIC_PACKAGE = 'django.views'


class BaseView(metaclass=ABCMeta):
    def get_import(self):
        text = 'from django.views import %s' % self.__class__.__name__
        return text

    @abstractmethod
    def get_main_text(self):
        pass

    def output(self, needs_import):
        text = ""
        if needs_import:
            text += self.get_import()

        text += self.get_main_text()
        return text


class View(BaseView):
    def get_main_text(self):
        text = "dispatch"
        return text


class FormView(BaseView):
    def get_main_text(self):
        text = "dispatch"
        return text


class CreateView(BaseView):
    def get_main_text(self):
        text = "dispatch"
        return text


class UpdateView(BaseView):
    def get_main_text(self):
        text = "dispatch"
        return text


class DetailView(BaseView):
    def get_main_text(self):
        text = "dispatch"
        return text


class DeleteView(BaseView):
    def get_main_text(self):
        text = "dispatch"
        return text


class TemplateView(BaseView):
    def get_main_text(self):
        text = "dispatch"
        return text


class ListView(BaseView):
    def get_main_text(self):
        text = "dispatch"
        return text
