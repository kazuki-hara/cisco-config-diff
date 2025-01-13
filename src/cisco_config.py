from utils.data_operations import count_space_num_from_head, update_dict_search_key_by_list

class CiscoConfig:
    def __init__(self, file_path:str, indent_space_num: int = 1):
        self.indent_space_num = indent_space_num
        self.config_text_list = None
        self.config_dict = None
        self.config_list = None
        self.read_text_file(file_path)
        self.convert_cisco_ios_config_to_dict()

    def read_text_file(self, file_path: str)-> None:
        with open(file=file_path, mode="r") as f:
            config_text_list = f.readlines()
        self.config_text_list = [config[:-1] for config in  config_text_list]
    
    def _convert_cisco_ios_config_to_dict(self)-> dict:
        dict_key_list = []
        for config in self.config_text_list:
            if config == "!" or not config:
                pass
            else:
                indent_depth = count_space_num_from_head(config) // self.indent_space_num
                if indent_depth == 0:
                    self.config_dict[config] = {}
                    dict_key_list = [config]
                    self.config_list.append(dict_key_list)
                else:
                    dict_key_list = dict_key_list[:indent_depth]
                    update_dict_search_key_by_list(self.config_dict, dict_key_list, config)

