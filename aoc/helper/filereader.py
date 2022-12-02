from pathlib import Path


def read_file(filepath: Path) -> list[str]:
    """Read a file from disk using filepath"""
    with open(filepath) as f:
        return f.readlines()
