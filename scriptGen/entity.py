# -*- coding:utf-8 -*-

# Created by Richard Liang at 2017/11/10
# Description:

from dao.tab_info import tabinfo
from util import cons_mapper, ucamel_convert, lcamel_convert, datatype_convert
from util.file_util import open_file

base_package_path, blank, br = cons_mapper()


def columns_gen(tab):
    paras = ''
    vars = []
    assignments = []
    getters_setters = []

    for tab_info in tab:
        column_name = tab_info[1]
        lc_column_name = lcamel_convert(column_name)
        uc_column_name = ucamel_convert(column_name)
        datatype = datatype_convert(tab_info[2])
        para = datatype + ' ' + lc_column_name
        assignment = 'this.' + lc_column_name + ' = ' + lc_column_name + ';'

        if tab_info[0] == 1:
            paras += para
        else:
            paras += ',' + para

        if tab_info[5] == 'auto_increment':
            vars.append('@Id\n@GeneratedValue\n')
        else:
            vars.append('@Column\n')

        if len(tab_info[4]) == 0:
            vars.append('private ' + para + ';\n')
        else:
            vars.append('private ' + para + ';  // ' + tab_info[4].replace('\n', ' ').replace('\r', ' ') + '\n')

        assignments.append(assignment + '\n')
        getters_setters.append(
            'public ' + datatype + ' get' + uc_column_name + '() {return ' + lc_column_name + ';}\n\n')
        getters_setters.append('public void set' + uc_column_name + '(' + para + '){' + assignment + '}\n\n')

    return paras, vars, assignments, getters_setters


def entity_gen(tableschema, tablename):
    uc_tablename = ucamel_convert(tablename)
    package_path = base_package_path + '.dao.entity'
    file = open_file(package_path, uc_tablename + 'Entity.java')

    paras, vars, assignments, getters_setters = columns_gen(tabinfo(tableschema, tablename))

    file.writelines('package' + blank + package_path + ';\n\n')
    file.writelines('import javax.persistence.*;' + '\n')
    file.writelines('import java.io.Serializable;' + '\n')
    file.writelines('import java.sql.Timestamp;' + '\n\n\n')
    file.writelines('@Entity\n')
    file.writelines('public class ' + uc_tablename + 'Entity implements Serializable {\n\n')
    for var in vars:
        file.writelines(var)
    file.writelines('\n')
    file.writelines('public ' + uc_tablename + 'Entity(){}\n\n')
    file.writelines('public ' + uc_tablename + 'Entity(' + paras + '){\n')
    for assignment in assignments:
        file.writelines(assignment)
    file.writelines('}\n\n')
    for getter_setter in getters_setters:
        file.writelines(getter_setter)
    file.writelines('}')

    file.close()


if __name__ == '__main__':
    entity_gen('Crawler', 'fixed_asset')
