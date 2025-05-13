mkdir data

# parser.py
from dataclasses import dataclass

@dataclass
class Frameglass:
    id: int
    tags: set

def parse_input(filepath: str) -> list:
    frameglasses = []
    with open(filepath, 'r') as file:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            parts = line.strip().split()
            tags = set(parts)
            frameglasses.append(Frameglass(id=idx, tags=tags))
    return frameglasses

