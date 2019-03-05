from abc import abstractmethod, ABCMeta
import textwrap


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
            text += '%s\n\n\n' % self.get_import()

        text += self.get_main_text()
        print(text)
        return text


class View(BaseView):
    def get_main_text(self):
        text = textwrap.dedent('''\
            class MyView(View):
                def dispatch(self, request, *args, **kwargs):
                    super().dispatch(request, *args, **kwargs)
                    # please implement here

                def http_method_not_allowed(self, request, *args, **kwargs):
                    # please implement here
                    super().http_method_not_allowed(request, *args, **kwargs)

                def get(self, request, *args, **kwargs):
                    # please implement here
                    pass

                def post(self, request, *args, **kwargs):
                    # please implement here
                    pass
        ''')
        return text


class FormView(BaseView):
    def get_main_text(self):
        text = textwrap.dedent('''\
            class MyFormView(FormView):
                # template_name = 'my_template.html'
                # form_class = 'MyForm'
                # success_url = '/my/success'

                def dispatch(self, request, *args, **kwargs):
                    super().dispatch(request, *args, **kwargs)
                    # please implement here

                def get_context_data(self, **kwargs):
                    context = super().get_context_data(**kwargs)
                    # please implement here
                    return context

                def form_valid(self, form):
                    form = super().form_valid(form)
                    # please implement here
                    return form

                def form_invalid(self, form):
                    form = super().form_invalid(form)
                    # please implement here
                    return form

                def get_success_url(self):
                    url = super().get_success_url()
                    # please implement here
                    return url
        ''')

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