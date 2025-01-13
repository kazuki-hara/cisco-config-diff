import difflib
import json
import re
from collections import deque
from pprint import pprint

from utils.data_operations import (count_space_num_from_head,
                                   update_dict_search_key_by_list,
                                   allkeys)


def read_text_file(file_path: str):
    with open(file=file_path, mode="r") as f:
        config_text_list = f.readlines()
    config_text_list = [config[:-1] for config in  config_text_list]
    return config_text_list



def convert_cisco_ios_config_to_dict(config_text_list: list, indent_space_num: int)-> dict:
    config_dict = {}
    dict_key_list = []
    for config in config_text_list:
        if config == "!" or not config:
            pass
        else:
            indent_depth = count_space_num_from_head(config) // indent_space_num
            if indent_depth == 0:
                config_dict[config] = {}
                dict_key_list = [config]
            else:
                dict_key_list = dict_key_list[:indent_depth]
                update_dict_search_key_by_list(config_dict, dict_key_list, config)
    return config_dict


def get_dict_diff(left_dict: dict, right_dict: dict):
    print(allkeys(left_dict))



if __name__=="__main__":
    before_config_text_list = read_text_file("tests/before.txt")
    before_config_dict = convert_cisco_ios_config_to_dict(config_text_list=before_config_text_list, indent_space_num=1)
    expect_config_text_list = read_text_file("tests/expect.txt")
    pprint(allkeys(before_config_dict))
    #pprint(before_only_dict)
    #pprint(expect_only_dict)