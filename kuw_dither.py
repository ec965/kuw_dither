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

    f: dict[str, float | str] = {
        "down": to_percent(down),
        "kuw": 3,
        "ordered-dither": "o8x8,3",
        "colors": 8,
        "interpolate": "Nearest",
        "filter": "Box",
        "up": to_percent(1 / down),
    }

    f = build_args(input, f, output_dir)
    convert_image(f)


def convert_image(args: dict[str, float | str]):
    convert = """convert {input} \\
      \\( -resize {down}% \\) \\
      \\( -kuwahara {kuw} \\) \\
      \\( -ordered-dither {ordered-dither} -colors {colors} \\) \\
      \\( -interpolate {interpolate} -filter {filter} \\) \\
      \\( -resize {up}% \\) \\
      {output}
      """.format(
        **args
    )

    os.system(convert)
    print("Finished:", args["output"])


def to_percent(n: float):
    return math.floor(n * 100)


def build_args(input: str, args: dict[str, float | str], output_dir: str = ""):
    args["output"] = build_output_path(input, args, output_dir)
    args["input"] = input
    return args


def build_output_path(input: str, args: dict[str, float | str], output_dir: str = ""):
    base, ext = input.split(".")
    out = os.path.join(output_dir, base)
    for k, v in args.items():
        out += f"_{k}_{v}"
    out += f".{ext}"
    return out


if __name__ == "__main__":
    main()
