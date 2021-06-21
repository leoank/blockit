"""CSV parser."""

from pathlib import Path
from typing import Dict

from blockit.txn.txn_chain import TransactionChain
from blockit.txn.txn_unit import TransactionUnit


def parse_mempool_csv(file_path: Path) -> Dict[str, TransactionChain]:
    """Parse mempool csv into Mempool class.

    Args:
        file_path (Path): Path of file to parse

    Returns:
        List[TransactionChain]: List of parsed transactions chains
    """
    with open(file_path) as csv:
        lines = csv.readlines()[1:]  # omit the headers

        # Create dict {"txn_id": "TransactionUnit"}
        txn_unit_dict = {
            line.strip().split(",")[0]: TransactionUnit(*line.strip().split(","))
            for line in lines
        }

        txn_chain_dict = {
            txid: txn_unit_to_chain(txn, txn_unit_dict)
            for txid, txn in txn_unit_dict.items()
        }
        return txn_chain_dict


def txn_unit_to_chain(
    txn: TransactionUnit, txn_unit_dict: Dict[str, TransactionUnit]
) -> TransactionChain:
    """Create txn chain from txn unit.

    Args:
        txn (TransactionUnit): Transaction
        txn_unit_dict (Dict[str, TransactionUnit]): Txn unit dict

    Returns:
        TransactionChain: TransactionChain
    """
    leaf_txn_id = txn.txid
    total_fee = txn.fee
    total_weight = txn.weight
    for parent in txn.parents:
        if txn_unit_dict.get(parent) is not None:
            total_fee += txn_unit_dict[parent].fee
            total_weight += txn_unit_dict[parent].weight
        else:
            txn.parents.remove(parent)
    return TransactionChain(
        txid=leaf_txn_id, fee=total_fee, weight=total_weight, parents=txn.parents
    )
