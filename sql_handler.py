from . import re
from . import data_type_conversions
import sqlite3 as sql
from .record import time_all_class_methods


@time_all_class_methods
class Sql:
    def __init__(self, database=None, console_output=False):
        self.master_table_dat = None
        self.console_output = console_output
        self.db = database
        self._set_con_and_cur()
        self._close_con_and_cur()

    def _close_con_and_cur(self):
        self.cur.close()
        self.conn.close()

    def _set_con_and_cur(self):
        self.conn = sql.connect(self.db)
        self.cur = self.conn.cursor()

    def run_query_text(self, query_text):
        self._set_con_and_cur()
        res = self.cur.execute(query_text)
        dat = res.fetchall()
        print(f'debug run query text before close\n{dat}')
        self._close_con_and_cur()
        print(f'debug run query text after close\n{dat}')
        print(dat)
        return dat

    def create_table(self, *args, **kwargs):
        print(args)
        for arg in args:
            print(f'arg: {arg}')
        for k, v in args:
            print(f'k: {k} | v: {v}')

        for kwarg in kwargs:
            print(f'kwarg: {kwarg} | kwargs[kwarg]: {kwargs[kwarg]}')
        for k, v in kwargs.items():
            print(f'k: {k} | v: {v}')

    def run_query_file(self, file_path):
        with open(file_path) as f:
            res = self.run_query_text(f.read())
            # print(f'debugging res var in run_query_file method\n{res}')
            return res

    def get_existing_tables(self):
        query_text = '''select * from sqlite_master'''
        self._set_con_and_cur()
        res = self.cur.execute(query_text)
        self.master_table_dat = res.fetchall()
        self._close_con_and_cur()
