def obtains_index_not_null(elements_list: list):
    return [i for i, x in enumerate(elements_list) if x is not None]


def obtains_index_null(elements_list: list):
    return [i for i, x in enumerate(elements_list) if x is None]
