
from producer_utils import get_value_from_config_file


def get_os(filepath):
    return get_value_from_config_file(filepath, 'OS')


def get_sw_ver(filepath):
    return get_value_from_config_file(filepath, 'Software')


def get_group(filepath):
    return get_value_from_config_file(filepath, 'GROUP')


if __name__ == '__main__':
    config_file = 'test/test_config'
    content = {"OS": get_os(config_file), "SW": get_sw_ver(config_file), "GROUP": get_group(config_file)}
    print content


