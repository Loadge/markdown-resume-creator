"""This file is the shiit."""
import sys
from pathlib import Path

repo_path = Path(__file__).parents[1]
sys.path.append(str(repo_path))

from config.config import load_configuration


if __name__== "__main__" :
    print("Hello world")

    load_configuration()


