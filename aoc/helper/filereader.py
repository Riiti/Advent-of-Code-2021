from pathlib import Path


def read_file(filepath: str) -> list[str]:
    """Read a file from disk using filepath"""
    path = Path(__file__).parent / filepath
    with open(path) as f:
        return f.readlines()
