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
    return value


def constructWrapper(cf):
    cof = cf

    def configWrapper(func, pathToCheck, elseFunc, boolean=True):
        section, filed = pathToCheck.split('.')
        value = cof[section][filed]
        if (boolean):
            if (toBool(value)):
                return func()
            else:
                return elseFunc()
        else:
            if (toBool(value)):
                return func()
    return configWrapper


def shouldShowSave(config, func, paramToCheck):
    if (toBool(config[paramToCheck])):
        func(config[paramToCheck])
