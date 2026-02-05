import sys
import argparse

def my_sum(arr):
    return sum(arr)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="*", type=int)
    args = parser.parse_args()    
    
    res = my_sum(args.numbers)
    print(f"Sum: {res}")

if __name__ == "__main__":
    main()