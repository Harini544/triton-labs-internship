"""Measure memory use for a lazy CSV batch iterator.

This script creates temporary CSV files, runs the iterator in batches, and
prints current and peak allocated memory using tracemalloc.
"""

from __future__ import annotations

import csv
import os
import tempfile
import tracemalloc
from pathlib import Path

from ml_data_loader.data_loader import LazyCSVBatchIterator


def build_csv_file(path: Path, rows: int) -> None:
    """Create a temporary CSV file with a simple schema."""
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["id", "name", "value"])
        for index in range(rows):
            writer.writerow([index, f"name_{index}", index * 2])


def measure_memory_for_dataset(size: int, batch_size: int = 100) -> tuple[float, float]:
    """Run the lazy iterator on a temporary dataset and report memory usage."""
    with tempfile.TemporaryDirectory() as temp_dir:
        folder = Path(temp_dir)
        csv_path = folder / "sample.csv"
        build_csv_file(csv_path, size)

        tracemalloc.start()
        iterator = LazyCSVBatchIterator(folder, batch_size=batch_size)
        for batch in iterator:
            _ = batch
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

    return current / (1024 * 1024), peak / (1024 * 1024)


def main() -> None:
    """Print measured memory for several dataset sizes."""
    print("Dataset Size | Batch Size | Current Memory (MB) | Peak Memory (MB)")
    print("---------------------------------------------------------------")

    for size in [100, 1000, 10000]:
        current, peak = measure_memory_for_dataset(size)
        print(f"{size:>12} | {100:>10} | {current:>18.4f} | {peak:>15.4f}")

    print("\nNotes:")
    print("- Exact numbers depend on the operating system, Python version, CSV content,")
    print("  batch size, and tracemalloc behavior.")
    print("- The important idea is that memory should not grow in direct proportion to the")
    print("  entire dataset when the implementation is truly lazy.")


if __name__ == "__main__":
    main()
