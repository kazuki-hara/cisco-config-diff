import pytest

from src.utils.data_operations import (
    count_space_num_from_head,
    update_dict_search_key_by_list,
)


def test_count_space_num_from_head():
    assert count_space_num_from_head("aaa") == 0
    assert count_space_num_from_head("aaa ") == 0
    assert count_space_num_from_head(" aaa") == 1
    assert count_space_num_from_head("  aaa") == 2
    assert count_space_num_from_head("  aaa a") == 2


def test_update_dict_search_key_by_list():
    assert update_dict_search_key_by_list(
        {"test1": {}, "test2": {}}, ["test1"], "test1-2"
    ) == {"test1": {"test1-2": {}}, "test2": {}}
    assert update_dict_search_key_by_list(
        {"test1": {"test1-2": {}}, "test2": {}}, ["test1", "test1-2"], "test1-3"
    ) == {"test1": {"test1-2": {"test1-3": {}}}, "test2": {}}
