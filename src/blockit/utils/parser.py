"""CSV parser."""

from pathlib import Path
from typing import List

from blockit.txn.txn_unit import TransactionUnit


def parse_mempool_csv(file_path: Path) -> List[TransactionUnit]:
    """Parse mempool csv into Mempool class.

    Args:
        file_path (Path): Path of file to parse

    Returns:
        List[TransactionUnit]: List of parsed transactions
    """
    with open(file_path) as csv:
        lines = csv.readlines()[1:]  # omit the headers
        txn_unit_list = [TransactionUnit(*line.strip().split(",")) for line in lines]
        return txn_unit_list
