# -*- coding: utf-8 -*-

import click

@click.command()
def main(args=None):
    """Console script for pyexample"""
    click.echo("Replace this message by putting your code into "
                "pyexample.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
