def read_file(filepath: str) -> list[str]:
    """Read a file from disk using filepath"""
    with open(filepath) as f:
        return f.readlines()
