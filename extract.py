from typing import NamedTuple
import argparse
from zipfile import ZipFile
from pathlib import Path


class Argument(NamedTuple):
    infile: str
    dest: str
    outfiles: list[str]


def extract_zip(arg: Argument):
    with ZipFile(arg.infile, "r") as zip:
        for outfile in arg.outfiles:
            dest_path = Path(arg.dest) / Path(outfile).name
            dest_path.write_bytes(zip.read(outfile))


def execute(arg: Argument):
    match (Path(arg.infile).suffix):
        case ".zip":
            extract_zip(arg)
        case _:
            raise NotImplementedError


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("dest")
    parser.add_argument("outfiles", nargs="*")
    args = Argument(**vars(parser.parse_args()))
    execute(args)
