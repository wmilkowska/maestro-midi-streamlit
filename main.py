import fortepyan as ff
from fortepyan.audio import render

from datasets import load_dataset


def main():
    dataset = load_dataset("roszcz/maestro-v1-sustain", split="train")

    return dataset
