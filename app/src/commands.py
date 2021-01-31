import click


@click.command()
def fun():
    """Description."""
    click.echo(click.style('fun', fg='blue'))
