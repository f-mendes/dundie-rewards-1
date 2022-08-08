import argparse

def load(filepath):
    with open(filepath) as file_:
        for line in file_:
            print(line)


def main():
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog="Enjoy and use with cautios.",
    )

    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load","show","send"),
        default="help"
    )
    parser.add_argument(
        "filepath",
        type=str,
        help="File path to load",
        default=None,
    )

    args = parser.parse_args()

    globals()[args.subcommand](args.filepath)
  
    

if __name__ == "__main__":
    main()