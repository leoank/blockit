"""Transaction block."""

from typing import List

from blockit.txn.txn_unit import TransactionUnit


class TransactionBlock:
    """Transaction block."""

    def __init__(self: "TransactionBlock") -> None:
        """Initialize block."""
        self.transactions: List[TransactionUnit] = []
        self.fee: int = 0
        self.count: int = 0
        self.size: int = 0

    def add_txn(self: "TransactionBlock", txn: TransactionUnit) -> None:
        """Add transaction to the block.

        Args:
            txn (TransactionUnit): Transaction to add
        """
        self.transactions.append(txn)
        self.fee += txn.fee
        self.count += 1
        self.size += txn.weight

    def __repr__(self: "TransactionBlock") -> str:
        """Repr TransactionBlock."""
        return f"""
            -------------------------
            Block Details
            -------------------------
            Size           = {self.size}
            Fee collected  = {self.fee}
            No. of Txns    = {self.count}
        """
