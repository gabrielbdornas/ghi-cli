def new_orphan_branch(subparsers):

    new_cmd = subparsers.add_parser("new-orphan-branch", help="Create a new orphan git branch.")
    new_cmd.add_argument("name")
    new_cmd.set_defaults(func=handle_command)


def handle_command(args):
    print(f"[GHI] Creating a new git orphan branch named {args.name}!")
