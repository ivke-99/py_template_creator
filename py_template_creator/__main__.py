import os
from cookiecutter.main import cookiecutter


def main():
    available_templates = next(os.walk('.'))[1]
    for i, template in enumerate(available_templates):
        print(f"ID: {i} -- Name: {template}")
    while True:
        try:
            choice = int(input("Pick a template ID from the list: "))
        except ValueError:
            print("Value is not an int. Retrying..")
            continue
        if choice > len(available_templates) - 1:
            print("Wrong id.")
        else:
            break
    cookiecutter(available_templates[choice])


if __name__ == '__main__':
    main()
