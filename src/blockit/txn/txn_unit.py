"""Transaction unit."""


class TransactionUnit:
    """Transaction unit."""

    def __init__(
        self: "TransactionUnit", txid: str, fee: str, weight: str, parents: str
    ) -> None:
        """Initialize transaction unit.

        Args:
            txid (str): Txn ID
            fee (str): fee of txn
            weight (str): weight of txn
            parents (str): parents of txn
        """
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = list(parents.split(";"))
