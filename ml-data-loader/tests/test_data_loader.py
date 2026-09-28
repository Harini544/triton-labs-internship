"""Tests for the lazy CSV batch loader."""

from pathlib import Path

import pytest

from ml_data_loader.data_loader import LazyCSVBatchIterator, lazy_csv_generator


def _write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        handle.write("id,name,value\n")
        for row in rows:
            handle.write(f"{row['id']},{row['name']},{row['value']}\n")


def test_reading_csv_files(tmp_path):
    csv_path = tmp_path / "sample.csv"
    _write_csv(csv_path, [{"id": "1", "name": "alpha", "value": "10"}])

    batches = list(LazyCSVBatchIterator(tmp_path, batch_size=10))

    assert len(batches) == 1
    assert batches[0][0]["name"] == "alpha"


def test_correct_number_of_rows(tmp_path):
    csv_path = tmp_path / "sample.csv"
    _write_csv(csv_path, [
        {"id": "1", "name": "a", "value": "1"},
        {"id": "2", "name": "b", "value": "2"},
        {"id": "3", "name": "c", "value": "3"},
    ])

    rows = []
    for batch in LazyCSVBatchIterator(tmp_path, batch_size=2):
        rows.extend(batch)

    assert len(rows) == 3


def test_correct_batch_size(tmp_path):
    csv_path = tmp_path / "sample.csv"
    rows = [{"id": str(i), "name": f"name_{i}", "value": str(i)} for i in range(5)]
    _write_csv(csv_path, rows)

    batches = list(LazyCSVBatchIterator(tmp_path, batch_size=2))

    assert [len(batch) for batch in batches] == [2, 2, 1]


def test_last_batch_smaller_than_batch_size(tmp_path):
    csv_path = tmp_path / "sample.csv"
    rows = [{"id": str(i), "name": f"name_{i}", "value": str(i)} for i in range(3)]
    _write_csv(csv_path, rows)

    batches = list(LazyCSVBatchIterator(tmp_path, batch_size=5))

    assert len(batches[-1]) == 3


def test_stop_iteration(tmp_path):
    csv_path = tmp_path / "sample.csv"
    _write_csv(csv_path, [{"id": "1", "name": "alpha", "value": "10"}])

    iterator = LazyCSVBatchIterator(tmp_path, batch_size=2)
    first = next(iterator)
    assert len(first) == 1

    with pytest.raises(StopIteration):
        next(iterator)


def test_generator_produces_expected_data(tmp_path):
    csv_path = tmp_path / "sample.csv"
    rows = [{"id": "1", "name": "alpha", "value": "10"}, {"id": "2", "name": "beta", "value": "20"}]
    _write_csv(csv_path, rows)

    generated = []
    for batch in lazy_csv_generator(tmp_path, batch_size=1):
        generated.extend(batch)

    assert generated[0]["name"] == "alpha"
    assert generated[-1]["name"] == "beta"


def test_empty_directory(tmp_path):
    iterator = LazyCSVBatchIterator(tmp_path, batch_size=5)
    assert list(iterator) == []


def test_multiple_csv_files(tmp_path):
    _write_csv(tmp_path / "a.csv", [{"id": "1", "name": "alpha", "value": "10"}])
    _write_csv(tmp_path / "b.csv", [{"id": "2", "name": "beta", "value": "20"}])

    batches = list(LazyCSVBatchIterator(tmp_path, batch_size=10))

    assert len(batches) == 2
    assert len(batches[0]) == 1
    assert len(batches[1]) == 1


def test_basic_lazy_behavior(tmp_path):
    csv_path = tmp_path / "sample.csv"
    _write_csv(csv_path, [{"id": "1", "name": "alpha", "value": "10"}, {"id": "2", "name": "beta", "value": "20"}])

    iterator = LazyCSVBatchIterator(tmp_path, batch_size=1)
    first_batch = next(iterator)
    second_batch = next(iterator)

    assert first_batch[0]["name"] == "alpha"
    assert second_batch[0]["name"] == "beta"


if __name__ == "__main__":
    pytest.main(["-q", __file__])
