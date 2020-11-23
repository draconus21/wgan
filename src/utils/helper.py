import os
import json
import logging
import logging.config

def setup_logging(path='logging.json',
                  level=logging.INFO,
                  env_key='LOG_CFG'):
    '''
    Setup logging
    '''
    value = os.getenv(env_key, None)
    if value is not None:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=level)

def getPadding(lvl, pad=' ', sep='\n'):
    string = ''
    if lvl > 0:
        string = pad*lvl + sep
    return string

def listToStr(tmpList, lvl=0, pad=' '):
    prntFmt = '{} '
    string = getPadding(lvl, pad) + '['
    for i, value in enumerate(tmpList):
        if isinstance(value, list):
            string = string + listToStr(value, lvl+1)
        else:
            string = string + prntFmt.format(value)
    string = string + ']'
    return string

def dictToStr(tmpDict, lvl=0, pad=' '):
    prntFmt = getPadding(lvl, pad) + '{}: {}'
    string = ''
    for key, value in tmpDict.items():
        if isinstance(value, dict):
            string = string + prntFmt.format(key, dictToStr(value, lvl+1))
        else:
            string = string + prntFmt(key, value)
    return string
