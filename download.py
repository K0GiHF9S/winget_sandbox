from typing import NamedTuple
import urllib.request
import argparse


class Argument(NamedTuple):
    url: str
    outfile: str


def execute(arg: Argument):
    with urllib.request.urlopen(arg.url) as res:
        data = res.read()
        with open(arg.outfile, mode="wb") as f:
            f.write(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("outfile")
    args = Argument(**vars(parser.parse_args()))
    execute(args)
