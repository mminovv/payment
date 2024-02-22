from click import Group

from src.core.cli.user import insert_user


def command_handler():
    group = Group()
    group.add_command(insert_user)
    return group


if __name__ == "__main__":
    registered = command_handler()
    registered()

