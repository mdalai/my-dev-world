
import os


def create_config_file(config_file):
    delete_config_file(config_file)

    lines = [
        "# comment line left space 0",
        "    # comment line left space 4",
        "",
        "OS=Windows 10",
        "Software = Spring Boot 3.11",
        "GROUP  =org.group ",
        " left white space = 1",
        "  left white space = 2",
        "     left white space = 5",
        "right white space = 1 ",
        "right white space = 3   ",
        "",
        "batch version=rls.120  ",
        "",
        "with no delimiter",
        "with no right value = ",
        " = with no left value",
    ]

    with open(config_file, 'a') as f:
        for line in lines:
            f.write(line + '\n')

    print("Config file created at: {}".format(config_file))


def delete_config_file(filepath):
    try:
        os.remove(filepath)
        print("Config file is removed: {}".format(filepath))
    except OSError:
        pass


if __name__ == '__main__':
    config_filepath = 'test_config'
    create_config_file(config_filepath)
