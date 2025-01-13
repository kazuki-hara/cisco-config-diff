from dictknife import deepmerge

def count_space_num_from_head(word: str)->int:
    index = 0
    space_num = 0
    while True:
        if word[index] == " ":
            space_num += 1
            index += 1
        else:
            break
    return space_num


def update_dict_search_key_by_list(d: dict, key_list: list, value: str) -> dict:
    add_dict = {}
    key_list.append(value)
    for key in reversed(key_list):
        _add_dict = add_dict.copy()
        add_dict.clear()
        add_dict[key] = _add_dict
    add_dict
    merged_dict = deepmerge(d, add_dict)
    return merged_dict