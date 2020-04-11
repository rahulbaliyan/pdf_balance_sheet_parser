"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "April 11 16:14:21 2020"
__copyright__ = "©2020 rahul_kumar"

"""
import numpy as np
import logging
logger = logging.getLogger(__name__)


class BalanceSheetQuery:
    @staticmethod
    def find_var(var, year, df):
        """
        This function return a query result

        :param year:
        :param var:
        :return:
        """
        try:
            df = df.apply(lambda x: x.astype(str).str.lower())
            nw_col_num = 0
            row_num, col_num = np.where(df == var.lower())
            col_list = {df.columns[col_num+1][0]: col_num + 1,
                        df.columns[col_num+2][0]: col_num + 2,
                        df.columns[col_num+3][0]: col_num + 3}
            for key, val in col_list.items():
                if key.isnumeric():
                    if int(key) == int(year):
                        nw_col_num = val
                        break
            result = df.iloc[row_num[0]][nw_col_num[0]]
            msg = var + ": " + str(result)
        except Exception as e:
            logger.error(str(e))
            msg = "No result found!"
        return msg