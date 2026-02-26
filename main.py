import argparse
from rich import print
from models.user import User
from models.project import Project
from models.task import Task

users = []

def add_user(args):
    user = User(args.name, args.email)
    users.append(user)
    print(f"[green]User created:[/green] {user}")

def list_users(args):
    for user in users:
        print(user)

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI")
    subparsers = parser.add_subparsers()

    # Add User
    parser_add_user = subparsers.add_parser("add-user")
    parser_add_user.add_argument("--name", required=True)
    parser_add_user.add_argument("--email", required=True)
    parser_add_user.set_defaults(func=add_user)

    # List Users
    parser_list_users = subparsers.add_parser("list-users")
    parser_list_users.set_defaults(func=list_users)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()