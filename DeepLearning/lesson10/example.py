import argparse
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--lr", type=float, default=1e-3)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = get_args()
    print(args.epochs)

