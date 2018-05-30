# encoding: utf-8

# Created by Richard Liang at 2017/11/9
# Description:

import os


def project_path():
    return os.path.abspath(os.path.dirname(__file__)).replace('/util', '')


def open_file(package_path, filename):
    dir = project_path() + '/output' + '/' + package_path.replace('.', '/')
    filename_full = dir + '/' + filename

    if os.path.exists(filename_full):
        os.remove(filename_full)

    if not os.path.isdir(dir):
        os.makedirs(dir)

    file = open(filename_full, 'w', encoding='utf8')

    return file


if __name__ == '__main__':
    file = open_file(project_path(),'test.java')
    file.writelines('DDD')
    file.close()
