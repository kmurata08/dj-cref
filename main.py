import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-type', type=str, help='the type of django generic view.')

    args = parser.parse_args()

    if not args.type:
        print('args.type is undefined.')


if __name__ == '__main__':
    main()
