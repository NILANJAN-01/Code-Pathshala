"""
Simple file I/O utilities.
"""
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Read and return text content from a file."""
    return Path(path).read_text(encoding=encoding)

def write_text(path: str | Path, content: str, encoding: str = "utf-8") -> None:
    """Write text content to a file safely."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding=encoding)
