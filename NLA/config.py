import configparser


def loadConfiguration(filename):
    config = configparser.ConfigParser()
    config.read(filename)
    return config


def toBool(value):
    if (value.lower() == 'true'):
        return True
    if (value.lower() == 'false'):
        return False
    else:
        print(value)
        raise "Invalid value in boolen expression!"
