import os
import sys
from importlib.machinery import SourceFileLoader

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TRANSLATE_PATH = os.path.join(ROOT_DIR, "Dataset", "animals", "translate.py")

if not os.path.exists(TRANSLATE_PATH):
    raise FileNotFoundError(f"Translator not found at {TRANSLATE_PATH}")

module = SourceFileLoader("animal_translate", TRANSLATE_PATH).load_module()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python translate.py <name>")
        sys.exit(1)

    source = sys.argv[1]
    print(module.translate_name(source))
