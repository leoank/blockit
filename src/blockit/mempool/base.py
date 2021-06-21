"""Base abstract Mempool class."""

from abc import ABC, abstractclassmethod
from pathlib import Path
from typing import List

from blockit.txn.txn_unit import TransactionUnit


class BaseMempool(ABC):
    """Base Mempool class."""

    @abstractclassmethod
    def load_txns(self: "BaseMempool", txns: List[TransactionUnit]) -> None:
        """Load txns data from CSV.

        Args:
            txns (List[TransactionUnit]): List of txns to load
        """
        pass

    @abstractclassmethod
    def build_block(self: "BaseMempool", block_limit: int) -> None:
        """Build best block.

        Args:
            block_limit (int): Limit of weight that can be added to the block
        """
        pass

    @abstractclassmethod
    def save_block(self: "BaseMempool", path: Path) -> None:
        """Save block.txt."""
        pass
