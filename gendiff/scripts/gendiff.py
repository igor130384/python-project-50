#!/usr/bin/env python3

from gendiff.scripts.cli import parse_args
from gendiff.scripts.generator import generate_diff


def main():
    args = parse_args()
    filename1, filename2 = args.filename1, args.filename2

    generate_diff(filename1, filename2)


if __name__ == '__main__':
    main()
