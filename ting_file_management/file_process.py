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
    file_length = instance.__len__()

    if file_length < 1:
        sys.stdout.write(str("Não há elementos\n"))
    else:
        remove_file = instance.dequeue()["nome_do_arquivo"]
        sys.stdout.write(str(f"Arquivo {remove_file} removido com sucesso\n"))


def file_metadata(instance, position):
    file_length = instance.__len__()

    if position < 0 or position > file_length:
        print("Posição inválida", file=sys.stderr)
    else:
        file = instance.search(position)
        sys.stdout.write(str(file))
