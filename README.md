# dj-cref
The output unit of Django generic view.

## Description
This is the Python package whose name is **dj-cref** .  
**dj-cref** outputs a template of django generic view you wanted.

![demo](https://raw.githubusercontent.com/wiki/Canon11/dj-cref/images/djcref.gif)


## Features
### Output kinds
- View
- FormView
- CreateView
- UpdateView
- DeleteView
- DetailView
- TemplateView
- ListView
- RedirectView

## Requirement
- Python3

## Usage
### Arguments
* <code>-type [kind of view]</code> : Which type of generic view to output.
* <code>--initial</code> : Whether to include import statements.

### Example
Case1
```
$ dj-cref -type FormView
class MyFormView(FormView):
    # template_name = 'my_template.html'
    # form_class = 'MyForm'
    # success_url = '/my/success'

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        # please implement here

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ...
```

Case2
```
$ dj-cref -type FormView --initial
from django.views import FormView


class MyFormView(FormView):
    # template_name = 'my_template.html'
    # form_class = 'MyForm'
    # success_url = '/my/success'

    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        ...
```

## Installation
```
$ pip install dj-cref
```

## Author
[@Canon11](https://github.com/Canon11/)
