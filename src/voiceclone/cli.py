"""CLI entrypoint for voiceclone."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from voiceclone import __version__


@click.group(name="voiceclone", invoke_without_command=True, no_args_is_help=True)
@click.version_option(__version__, prog_name="voiceclone")
@add_tree_option(renderer_options={"root_name": "voiceclone"})
def main() -> None:
    """voiceclone command line interface."""
    # Add package-specific commands here. Prefer ChatStyle helpers for
    # interactive input when a command needs recoverable user input.
    pass


if __name__ == "__main__":
    main()
