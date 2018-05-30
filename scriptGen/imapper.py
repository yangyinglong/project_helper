# coding:utf-8

from dao.tab_info import tabinfo
from util import cons_mapper, ucamel_convert, lcamel_convert, datatype_convert
from util.file_util import open_file

base_package_path, blank, br = cons_mapper()


def columns(tab):
    columns_query = ''
    columns_insert = ''
    columns_update = ''

    for i, tab_info in enumerate(tab):
        column_name = tab_info[1]
        if i + 1 < len(tab):
            columns_query += '`' + column_name + '`' + ', '
            columns_insert += '#{' + lcamel_convert(column_name) + '}' + ', '
            columns_update += column_name + '=#{' + lcamel_convert(column_name) + '}' + ', '
        else:
            columns_query += '`' + column_name + '`'
            columns_insert += '#{' + lcamel_convert(column_name) + '}'
            columns_update += column_name + '=#{' + lcamel_convert(column_name) + '}'

    return columns_query, columns_insert, columns_update


def keys(tab):
    keys_exp = ''
    keys_para = ''

    for i, tab_info in enumerate(tab):
        column_name = tab_info[1]
        lc_column_name = lcamel_convert(column_name)
        if tab_info[3] == 'PRI':
            if i == 0:
                keys_exp += '`' + column_name + '` = #{' + lc_column_name + '}'
                keys_para += '@Param("' + lc_column_name + '") ' + datatype_convert(tab_info[2]) + ' ' + lc_column_name
            else:
                keys_exp += ' and `' + column_name + '` = #{' + lc_column_name + '}'
                keys_para += ', +@Param("' + lc_column_name + '") ' + datatype_convert(
                    tab_info[2]) + ' ' + lc_column_name

    return keys_exp, keys_para


def results_gen(tab):
    list = []
    results = ''

    list.append('@Results({')
    for i, tab_info in enumerate(tab):
        column_name = tab_info[1]
        lc_column_name = lcamel_convert(column_name)
        if i + 1 < len(tab):
            list.append('@Result(property = "' + lc_column_name + '", column = "' + tab_info[1] + '"), ')
        else:
            list.append('@Result(property = "' + lc_column_name + '", column = "' + tab_info[1] + '")')

    list.append('})')

    for item in list:
        results += item + '\n'

    return results


def imapper_gen(tableschema, tablename):
    uc_tablename = ucamel_convert(tablename)
    tab = tabinfo(tableschema, tablename)
    columns_query, columns_insert, columns_update = columns(tab)
    keys_exp, keys_para = keys(tab)
    package_path = base_package_path + '.dao.mapper'
    file = open_file(package_path, 'I' + uc_tablename + 'Mapper.java')

    file.writelines('package' + blank + package_path + ';\n\n')
    file.writelines('import' + blank + base_package_path + '.dao.entity.' + uc_tablename + 'Entity;\n')
    file.writelines('import org.apache.ibatis.annotations.*;' + '\n')
    file.writelines('import java.util.List;' + '\n\n\n')
    file.writelines('@Mapper\n')
    file.writelines('public interface I' + uc_tablename + 'Mapper {\n')
    file.writelines(
        '@Select("SELECT ' + columns_query + ' FROM `' + tablename + '`")' + '\n' +
        results_gen(tab) +
        'List<' + uc_tablename + 'Entity> queryAll();\n')
    file.writelines(
        '@Select("SELECT ' + columns_query + ' FROM `' + tablename + '` WHERE ' + keys_exp + '")' + '\n' +
        results_gen(tab) +
        uc_tablename + 'Entity queryByKey(' + keys_para + ');\n\n')
    file.writelines(
        '@Insert("INSERT INTO `' + tablename + '(' + columns_query + ')` VALUES(' + columns_insert + ')")\n')
    file.writelines('void insert(' + uc_tablename + 'Entity ' + tablename + 'Entity);\n\n')
    file.writelines('@Update("UPDATE `' + tablename + '` SET ' + columns_update + ' WHERE ' + keys_exp + '")\n' +
                    'void update(' + uc_tablename + 'Entity ' + tablename + 'Entity);\n\n')
    file.writelines('@Delete("DELETE FROM `' + tablename + '` WHERE ' + keys_exp + '")\n' +
                    'void delete(' + keys_para + ');\n\n')
    file.writelines('}')

    file.close()


if __name__ == '__main__':
    imapper_gen('Crawler', 'fixed_asset')
