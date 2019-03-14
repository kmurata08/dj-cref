import argparse
from .runner import (
    View, FormView, CreateView, UpdateView, DetailView,
    DeleteView, TemplateView, ListView, RedirectView
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-type', type=str, help='the type of django generic view.')
    parser.add_argument(
        '--initial', action='store_true', help='either import or not'
    )

    args = parser.parse_args()

    if args.type:
        run(args.type, args.initial)
    else:
        print('args.type is undefined.')


def run(t, exists_initial):
    if t == 'View':
        view = View()
    elif t == 'FormView':
        view = FormView()
    elif t == 'CreateView':
        view = CreateView()
    elif t == 'UpdateView':
        view = UpdateView()
    elif t == 'DetailView':
        view = DetailView()
    elif t == 'DeleteView':
        view = DeleteView()
    elif t == 'TemplateView':
        view = TemplateView()
    elif t == 'ListView':
        view = ListView()
    elif t == 'RedirectView':
        view = RedirectView()
    else:
        print('type is invalid.')
        return

    view.output(exists_initial)


if __name__ == '__main__':
    main()
