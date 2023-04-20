#!/usr/bin/env python3

from gendiff.cli import parse_args
from gendiff.generator import generate_diff


def main():
    args = parse_args()
    print(
        generate_diff(args.filename1, args.filename2))


if __name__ == '__main__':
    main()