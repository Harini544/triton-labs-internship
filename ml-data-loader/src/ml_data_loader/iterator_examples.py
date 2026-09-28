"""Examples of iterator utilities and lazy iteration patterns."""

from __future__ import annotations

from itertools import chain, islice


try:
    from itertools import batched
except ImportError:
    batched = None


def demo_islice(values, size):
    """Show how islice keeps only a window of values."""
    return list(islice(values, size))


def demo_chain(first, second):
    """Show how chain joins multiple iterables."""
    return list(chain(first, second))


def demo_batched(values, batch_size):
    """Demonstrate batch creation.

    Python 3.12 added itertools.batched. If it is unavailable, a compatibility
    helper can be used instead.
    """
    if batched is not None:
        return list(batched(values, batch_size))

    result = []
    iterator = iter(values)
    while True:
        chunk = tuple(islice(iterator, batch_size))
        if not chunk:
            break
        result.append(chunk)
    return result


__all__ = ["demo_islice", "demo_chain", "demo_batched"]
