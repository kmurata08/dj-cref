import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-type', type=str, help='the type of django generic view.')

    args = parser.parse_args()

    if args.type:
        run(args.type)
    else:
        print('args.type is undefined.')


def run(t):
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
    elif t == 'TemplaveView':
        view = TemplateView()
    elif t == 'ListView':
        view = ListView()
    else:
        print('type is invalid.')
        return

    view.output()


if __name__ == '__main__':
    main()
