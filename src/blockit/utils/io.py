"""File I/O util  functions."""

from pathlib import Path

from blockit.txn.txn_block import TransactionBlock


def get_project_root_path() -> Path:
    """Get project root path.

    Returns:
        Path: Absolute path of the project root
    """
    return Path(__file__).parents[3].absolute()


def write_block(txn_block: TransactionBlock, path: Path = None) -> None:
    """Save transaction block.

    Args:
        txn_block (TransactionBlock): Transaction block to save
        path (Path): Path to save file
    """
    txn_ids = []
    for txn in txn_block.transactions:
        txn_ids.append(txn.txid)
    if path is None:
        save_path = get_project_root_path() / "block.txt"
    else:
        save_path = path
    with open(save_path, "w") as f:
        for txn_id in txn_ids:
            f.write(f"{txn_id}\n")
