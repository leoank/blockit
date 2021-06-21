"""Transaction block."""

from typing import Dict, List

from blockit.txn.txn_chain import TransactionChain


class TransactionBlock:
    """Transaction block."""

    def __init__(self: "TransactionBlock") -> None:
        """Initialize block."""
        self.transactions: List[TransactionChain] = []
        self.transactions_lookup: Dict[str, int] = {}
        self.fee: int = 0
        self.count: int = 0
        self.size: int = 0

    def add_txn(
        self: "TransactionBlock",
        txn: TransactionChain,
        txns: Dict[str, TransactionChain],
    ) -> None:
        """Add transaction to the block.

        Args:
            txn (TransactionChain): Transaction to add
            txns (Dict[str, TransactionChain]): Dict for Transaction lookup
        """
        for parent in txn.chain:
            if self.transactions_lookup.get(parent) is None:
                self.transactions.append(txns[parent])
                self.transactions_lookup[parent] = 1
                self.count += 1
        if self.transactions_lookup.get(txn.txid) is None:
            self.transactions.append(txn)
            self.transactions_lookup[txn.txid] = 1
            self.count += 1
        self.fee += txn.fee
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
