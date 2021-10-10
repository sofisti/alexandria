import click

from utils import generate_models


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option("--model", default="")
@click.option("--path", default="")
@click.option("--indent", default=0, type=int)
def generate(model: str, path: str, indent: int) -> None:
    generate_models(model, path, int(indent))


@cli.command(name="write")
@click.option("--path", default=".cache/schema")
def write(path: str) -> None:
    generate_models("", path, 2)


if __name__ == "__main__":
    cli()
