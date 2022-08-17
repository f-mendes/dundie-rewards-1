import pkg_resources
import rich_click as click
from rich.console import Console
from rich.table import Table

from dundie import core

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


@click.group()
@click.version_option(version=pkg_resources.get_distribution("dundie").version)
def main():
    """Dunder Mifflin Rewards System

    This cli aplication controls DM rewards system.
    """


@main.command()
@click.argument("filepath", type=click.Path(exists=True))
def load(filepath):
    """Loads the file to the database.
    ## Features
    - Validates data.
    - Parses the file.
    - Loads to database.
    """

    table = Table(title="Dunder Mifflin Associates")
    header = ["name", "dept", "role", "e-mail"]
    for head in header:
        table.add_column(head, style="magenta")

    result = core.load(filepath)
    for person in result:
        table.add_row(*[row.strip() for row in person.split(",")])

    console = Console()
    console.print(table)
