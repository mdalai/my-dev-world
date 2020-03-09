
def run_cmd_and_extract(cmd_str, match):
    pass


def parse_config_file(config_filepath, delimiter="=", comment_prefix="#"):
    """
    :param config_filepath: filepath
    :param delimiter: can be = or :
    :param comment_prefix:  # or //
    :return: dict
    """
    keyvals = {}
    with open(config_filepath) as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.strip()
            if not line or line.startswith(comment_prefix):
                continue
            p = [p.strip() for p in line.split(delimiter)]
            if len(p) < 2 or not p[0]:
                continue
            keyvals[p[0]] = p[1]
    return keyvals


def get_value_from_config_file(config_filepath, key_str):
    key_values = parse_config_file(config_filepath)
    return key_values[key_str]


if __name__ == '__main__':
    config_file = 'test/test_config'
    key_vals = parse_config_file(config_file)
    print key_vals
