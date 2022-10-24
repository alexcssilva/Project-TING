from os.path import exists
import sys


def txt_importer(path_file):
    if not exists(path_file):
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None

    if '.txt' not in path_file:
        print("Formato inválido", file=sys.stderr)
        return None

    with open(path_file, "r") as path:
        return path.read().split("\n")
