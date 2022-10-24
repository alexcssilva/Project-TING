import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for row in range(len(instance)):
        if instance.search(row)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(result)

    sys.stdout.write(str(result))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
