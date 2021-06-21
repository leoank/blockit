"""Command-line interface."""
# flake8: noqa

from pathlib import Path

import click

from .. import __version__

from blockit.utils.parser import parse_mempool_csv
from blockit.mempool.sdt import SDTMempool


@click.command()
@click.argument("file")
def sdt(file) -> None:
    """invoke sdt implementation."""
    mempool_path = Path(file)
    click.secho(f"Loading mempool csv from {mempool_path}")

    sdt_mempool = SDTMempool(
        size_class=200, density_class=200, size_upper=1350, density_upper=0.0015
    )

    click.secho("Parsing txns from mempool csv")
    txns_list = parse_mempool_csv(mempool_path)

    click.secho("Loading txns into SDT mempool")
    sdt_mempool.load_txns(txns_list)
    click.secho(f"{sdt_mempool.__repr__()}")

    click.secho("Building best block")
    sdt_mempool.build_block(block_limit=4000000)
    click.secho(f"{sdt_mempool.block.__repr__()}")

    click.secho("Saving block")
    sdt_mempool.save_block()

    pass


@click.group()
@click.version_option(version=__version__)
def main() -> None:
    """Blockit console."""
    pass


main.add_command(sdt)
