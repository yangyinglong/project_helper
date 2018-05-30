# encoding: utf-8

# Created by Richard Liang at 2017/11/8
# Description:

import yaml

from util.file_util import project_path


def add_semicolon(val):
    if val != '}' and val != '{':
        return val + ';'
    else:
        return val


def cons_mapper():
    with open(project_path() + '/resources' + '/cons.yaml', 'r') as f:
        mapper = yaml.load(f.read())['mapper']
        base_package_path = mapper['base_package_path']
        blank = mapper['blank']
        br = mapper['br']

        return base_package_path, blank, br


def db_url():
    with open(project_path() + '/resources' + '/dbconn.yaml', 'r') as f:
        yaml.load(f.read())

        return yaml.load(f.read())


def ucamel_convert(para):
    rslt = ''
    if para != None or para.strip() != '':
        para_splits = para.split('_')
        for para_split in para_splits:
            rslt += para_split[:1].upper() + para_split[1:]

    return rslt


def lcamel_convert(para):
    return ucamel_convert(para)[:1].lower() + ucamel_convert(para)[1:]


def datatype_convert(datatype):
    if datatype.find('int', ) >= 0:
        return 'Integer'
    elif datatype.find('char', ) >= 0:
        return 'String'
    elif datatype == 'datetime':
        return 'Timestamp'
    else:
        return 'String'


if __name__ == '__main__':
    s = 'FuncNameIsLongLong'
    print(ucamel_convert(s))
    print(lcamel_convert(s))
