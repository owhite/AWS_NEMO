#!/usr/bin/env python3

import sys
import fnmatch


BLOCK_PATTERNS = {
    "demultiplexed_fastq/",
    "VISp/",
    "raw/",
    "mtg/",
    "CellRanger5/",
    "multimodal/",
    "marmoset1/",
    "marmoset2/",
    "counts/",
    "align/",
    "cells/",
    "u19_cemba/",
    "nuclei/",
}


def indent_level(line: str) -> int:
    """Count leading spaces."""
    return len(line) - len(line.lstrip(" "))


def normalize_name(name: str) -> str:
    """
    Normalize a tree entry for matching.
    Keeps internal characters intact, removes surrounding whitespace.
    """
    return name.strip()


def is_blocked_name(name: str) -> bool:
    """Return True if the name matches any block pattern."""
    normalized = normalize_name(name)
    return any(fnmatch.fnmatch(normalized, pattern) for pattern in BLOCK_PATTERNS)


def filter_tree(lines) -> None:
    """
    Print the tree, but suppress anything deeper than a blocked node.
    The blocked node itself is printed.
    If suppressed children exist, print:
        SEQUENCE_DIRECTORIES:NUM
    at the child indentation level.
    """
    blocking = False
    block_indent = 0
    blocked_count = 0

    for raw_line in lines:
        line = raw_line.rstrip("\n")

        if not line.strip():
            if not blocking:
                print()
            continue

        current_indent = indent_level(line)
        stripped = normalize_name(line)

        if blocking:
            if current_indent > block_indent:
                blocked_count += 1
                continue
            else:
                if blocked_count > 0:
                    print(f"{' ' * (block_indent + 4)}SEQUENCE_DIRECTORIES:{blocked_count}")
                blocking = False
                blocked_count = 0

        print(line)

        if is_blocked_name(stripped):
            blocking = True
            block_indent = current_indent
            blocked_count = 0

    if blocking and blocked_count > 0:
        print(f"{' ' * (block_indent + 4)}SEQUENCE_DIRECTORIES:{blocked_count}")


def main() -> int:
    if len(sys.argv) > 2:
        print(f"Usage: {sys.argv[0]} [tree_file]", file=sys.stderr)
        return 1

    if len(sys.argv) == 2:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            filter_tree(f)
    else:
        filter_tree(sys.stdin)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
