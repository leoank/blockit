"""SDT mempool implementation.

Size-density table(SDT) strategy for selecting cryptocurrency
Transactions from mempool that improves on the standard heap
sort by reducing runtime from O(nlogn) to O(n).

journal reference: https://doi.org/10.1109/Blockchain.2019.00024
implementation by author: https://github.com/ChuksXD/SDT-Blockchain
"""

import math
from pathlib import Path
from typing import List

from blockit.mempool.base import BaseMempool
from blockit.txn.txn_block import TransactionBlock
from blockit.txn.txn_unit import TransactionUnit
from blockit.utils.io import write_block


class SDTMempool(BaseMempool):
    """SDT mempool."""

    def __init__(
        self: "SDTMempool",
        size_class: int,
        density_class: int,
        size_upper: int,
        density_upper: int,
    ) -> None:
        """Initialize SDT.

        Args:
            size_class (int): Size class
            density_class (int): Density class
            size_upper (int): Upper limit of size class
            density_upper (int): Upper limit of density class
        """
        self.size_class_limit = size_class
        self.density_class_limit = density_class
        self.size_upper = size_upper
        self.density_upper = density_upper
        self.table = [
            [[] for x in range(self.density_class_limit)]
            for y in range(self.size_class_limit)
        ]
        self.sizeTable = [
            [0 for x in range(self.density_class_limit)]
            for y in range(self.size_class_limit)
        ]
        self.count = 0
        self.block = TransactionBlock()

    def load_txns(self: "SDTMempool", txns: List[TransactionUnit]) -> None:
        """Load txns data from CSV.

        Args:
            txns (List[TransactionUnit]): List of txns to load
        """
        for txn in txns:
            self.count += 1
            density = txn.fee / txn.weight
            densityScaled = density / self.density_upper
            sizeScaled = txn.weight / self.size_upper
            if densityScaled >= 1:
                density_class = self.density_class_limit - 1
            else:
                density_class = math.floor(
                    densityScaled * (self.density_class_limit - 1)
                )
            if sizeScaled >= 1:
                size_class = self.size_class_limit - 1
            else:
                size_class = math.floor(
                    (txn.weight / self.size_upper) * (self.size_class_limit - 1)
                )

            self.table[size_class][density_class].append(txn)
            self.sizeTable[size_class][density_class] += txn.weight

    def build_block(self: "BaseMempool", block_limit: int) -> None:
        """Build best block.

        Args:
            block_limit (int): Limit of weight that can be added to the block
        """
        cap = block_limit - self.block.size
        terminated = False
        j = self.density_class_limit - 1
        while not terminated and j >= 0:
            index = cap / self.density_upper  # empty fraction of the block
            if index >= 1:
                si = self.size_class_limit - 1
            else:
                si = math.floor(
                    index * (self.size_class_limit - 1)
                )  # class which cap belongs
            selected = False
            i = si - 1

            while i >= 0 and not selected:
                if len(self.table[i][j]) > 0:
                    x = self.table[i][j].pop()
                    self.block.add(x)
                    selected = True
                else:
                    i -= 1

            if not selected:
                for item in range(len(self.table[si][j])):
                    if self.table[si][j][item].weight <= cap:
                        self.block.add(self.table[si][j][item])
                        self.table[si][j].pop(item)
                        selected = True
                        break
            if not selected:
                j -= 1
            else:
                cap = block_limit - self.block.size
                if cap < 100:
                    terminated = True

    def save_block(self: "BaseMempool", path: Path = None) -> None:
        """Save block.txt.

        Args:
            path (Path): Path to save file. Defaults to None.
        """
        write_block(self.block, path)

    def __repr__(self: "SDTMempool") -> str:
        """Repr SDTMempool."""
        return f"""
            ---------------------------
            SDT Details
            ---------------------------
            Table length          ={len(self.table)}
            No .of txns           ={self.count}
            Size class limit      ={self.size_class_limit}
            Size upper            ={self.size_upper}
            Denisity class limit  ={self.density_class_limit}
            Density upper         ={self.density_upper}
        """
