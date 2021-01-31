import click

from app.src.commands import fun


@click.group()
def cli():
    """Description."""
    pass


cli.add_command(fun)

if __name__ == '__main__':
    cli(obj={})
