#!/usr/bin/env python3

import sys
import os
import math


def main():
    if len(sys.argv) < 2:
        print("Please provide an input file")
        exit(1)

    input = sys.argv[1]
    output_dir = "out"

    down = 1 / 2

    f = [
        {"resize": f"{to_percent(down)}%"},
        {"kuwahara": 1},
        {"ordered-dither": "o8x8,3", "colors": 8},
        {"interpolate": "Nearest", "filter": "Box"},
        {"resize": f"{to_percent(1/down)}%"},
    ]

    result = convert_img(input, output_dir, f)
    print("Finished: ", result)


def convert_img(input_path: str, output_dir: str, params: list[dict[str, float | str]]):
    name, ext = os.path.basename(input_path).split(".")

    cmd = [f"convert {input_path}"]
    for p in params:
        cmd.append("\\(")
        for k, v in p.items():
            cmd.append(f"-{k} {v}")
            name += f"_{k}_{v}"
        cmd.append("\\)")

    name += f".{ext}"
    name = os.path.join(output_dir, name)

    cmd.append(name)

    c = " ".join(cmd)
    os.system(c)

    return name


def to_percent(n: float):
    return math.floor(n * 100)


if __name__ == "__main__":
    main()
