import typer
from typing import Annotated


class WordCount:
    def __init__(self):
        self.app = typer.Typer()

    @staticmethod
    def _read_file(filename):
        with open(filename, "rb") as file:
            return file.read()

    def byte_count(self, filename):  # m
        data = self._read_file(filename)
        count = len(data)
        typer.echo(f"Number of bytes in the file {filename}: {count}")

    def character_count(self, filename):  # c
        data = self._read_file(filename)
        count = sum(1 for char in data if char != b"\n")
        typer.echo(f"Number of characters in the file {filename}: {count}")

    def line_count(self, filename):  # l
        with open(filename, "r") as file:
            count = len(file.readlines())
        typer.echo(f"Number of lines in the file {filename}: {count}")

    def word_count(self, filename):  # w
        with open(filename, "r") as file:
            data = file.read()
            word_count = len(data.split())
        typer.echo(f"Number of words in file {filename}: {word_count}")


def main():
    wc = WordCount()

    @wc.app.command("m")
    def byte_count_cli(filename: Annotated[str, typer.Argument()] = None):
        wc.byte_count(filename)

    @wc.app.command("c")
    def character_count_cli(filename: Annotated[str, typer.Argument()] = None):
        wc.character_count(filename)

    @wc.app.command("l")
    def line_count_cli(filename: Annotated[str, typer.Argument()] = None):
        wc.line_count(filename)

    @wc.app.command("w")
    def word_count_cli(filename: Annotated[str, typer.Argument()] = None):
        wc.word_count(filename)

    wc.app()


if __name__ == "__main__":
    main()