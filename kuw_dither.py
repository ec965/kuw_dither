#!/usr/bin/env python3

import sys
import os
import math


def to_percent(n: float):
    return math.floor(n * 100)


def build_output(input: str, args: dict[str, float | str], output_dir: str = ""):
    base, ext = input.split(".")
    out = os.path.join(output_dir, base)
    for k, v in args.items():
        out += f"_{k}_{v}"
    out += f".{ext}"
    return out


if len(sys.argv) < 2:
    print("Please provide an input file")
    exit(1)

input = sys.argv[1]
output_dir = "out"

down = 1 / 2

f: dict[str, float | str] = {
    "down": to_percent(down),
    "kuw": 1,
    "dither": "Riemersma",
    "colors": 32,
    "interpolate": "Nearest",
    "filter": "Box",
    "up": to_percent(1 / down),
}

f["output"] = build_output(input, f, output_dir)
f["input"] = input

convert = """convert {input} \\
  \\( -resize {down}% -kuwahara {kuw} \\) \\
  \\( -dither {dither} -colors {colors} \\) \\
  \\( -interpolate {interpolate} -filter {filter} -resize {up}% \\) \\
  {output}
  """.format(
    **f
)

os.system(convert)
