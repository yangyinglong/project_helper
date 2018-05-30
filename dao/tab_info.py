# -*- coding: UTF-8 -*-
import pymysql


# TODO Will be replaced by SQLAlchemy for multi-connection issue
def tabinfo(tableschema, tablename):
    conn = pymysql.connect(host='122.144.217.112',
                           port=13306, user='pc_user1',
                           passwd='PPydckke8762',
                           db='information_schema',
                           charset='utf8')

    cursor = conn.cursor()
    sql = "select ORDINAL_POSITION,COLUMN_NAME,DATA_TYPE,COLUMN_KEY,COLUMN_COMMENT,EXTRA \
               from information_schema.columns \
               where table_schema = '%s' \
               and table_name = '%s';" % (tableschema, tablename)
    try:
        cursor.execute(sql)

        return cursor.fetchall()

    except:
        print("Error: unable to fecth data")
    finally:
        conn.close()


if __name__ == '__main__':
    for i, tab_info in enumerate(tabinfo('Crawler', 'fixed_asset')):
        print(i, tab_info)
