"""Lazy CSV batch loading examples for learning iterators and generators."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterator, List, Iterable


class LazyCSVBatchIterator:
    """Iterate over CSV files in a directory one batch at a time.

    This class shows the Python iterator protocol using __iter__ and __next__.
    It reads files lazily, so it does not load the full dataset into memory.
    """

    def __init__(self, folder_path: str | Path, batch_size: int = 100):
        self.folder_path = Path(folder_path)
        self.batch_size = batch_size
        self._file_paths = sorted(self.folder_path.glob("*.csv"))
        self._file_index = 0
        self._current_reader = None
        self._current_handle = None
        self._current_batch = []

        if batch_size <= 0:
            raise ValueError("batch_size must be greater than 0")

    def __iter__(self) -> "LazyCSVBatchIterator":
        """Return the iterator object itself.

        The for loop calls __iter__() first. This lets Python know how to
        start iteration. The iterator should return itself so that the loop can
        repeatedly call __next__() until iteration is finished.
        """
        self._file_index = 0
        self._current_batch = []
        self._current_reader = None
        if self._current_handle is not None:
            self._current_handle.close()
            self._current_handle = None
        return self

    def __next__(self) -> list[dict[str, str]]:
        """Return one batch of rows at a time.

        __next__() is the method that actually produces the next item in the
        sequence. When there are no more rows, it raises StopIteration. That
        signal tells a for loop to stop iterating.
        """
        while True:
            if self._current_reader is None:
                if self._file_index >= len(self._file_paths):
                    if self._current_batch:
                        batch = self._current_batch
                        self._current_batch = []
                        return batch
                    raise StopIteration

                csv_path = self._file_paths[self._file_index]
                self._current_handle = csv_path.open("r", newline="", encoding="utf-8")
                self._current_reader = csv.DictReader(self._current_handle)
                self._file_index += 1

            try:
                row = next(self._current_reader)
            except StopIteration:
                if self._current_handle is not None:
                    self._current_handle.close()
                    self._current_handle = None
                self._current_reader = None

                if self._current_batch:
                    batch = self._current_batch
                    self._current_batch = []
                    return batch
                continue

            self._current_batch.append(row)
            if len(self._current_batch) == self.batch_size:
                batch = self._current_batch
                self._current_batch = []
                return batch

    def _read_all_rows(self) -> list[dict[str, str]]:
        """Helper for simple tests and quick inspection."""
        rows: list[dict[str, str]] = []
        for batch in self:
            rows.extend(batch)
        return rows


def lazy_csv_generator(folder_path: str | Path, batch_size: int = 100) -> Iterator[list[dict[str, str]]]:
    """Yield CSV rows in batches using a generator.

    A generator function uses the yield keyword. Unlike return, a generator
    pauses its work and resumes later. This makes it lazy: values are produced
    only when the caller asks for them.
    """
    folder = Path(folder_path)
    for csv_path in sorted(folder.glob("*.csv")):
        with csv_path.open("r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            batch: list[dict[str, str]] = []
            for row in reader:
                batch.append(row)
                if len(batch) == batch_size:
                    yield batch
                    batch = []
            if batch:
                yield batch


__all__ = ["LazyCSVBatchIterator", "lazy_csv_generator"]
