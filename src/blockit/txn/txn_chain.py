"""Transaction chain."""


from typing import List


class TransactionChain:
    """Transaction chain."""

    def __init__(
        self: "TransactionChain",
        txid: str,
        fee: str,
        weight: str,
        parents: List[str],
    ) -> None:
        """Initialize transaction chain.

        Args:
            txid (str): Txn ID
            fee (str): fee of all txns
            weight (str): weight of all txns
            parents (str): parents of txn
        """
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.chain = parents
