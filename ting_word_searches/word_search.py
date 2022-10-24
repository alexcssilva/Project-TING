def exists_word(word, instance):
    word_list = list()

    for row in range(instance.__len__()):
        file = instance.search(row)
        occurrence_list = list()
        rows = file["linhas_do_arquivo"]

        for row, line in enumerate(rows):
            if (word.lower() in line.lower()):
                occurrence_list.append({"linha": row + 1})

        if (len(occurrence_list) > 0):
            result = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrence_list
            }
            word_list.append(result)
    return word_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
