"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "April 11 10:48:15 2020"
__copyright__ = "©2020 rahul_kumar"
"""

from tabula import read_pdf
import logging


class UserPdfParser:

    logger = logging.getLogger(__name__)

    @staticmethod
    def read_pdf_to_df(path):
        """
        This function reads a pdf and return a dataframe

        :param path:
        :return:
        """
        try:
            df = read_pdf(path)
            return df
        except Exception as e:
            UserPdfParser.logger.error(str(e))

    @staticmethod
    def data_preprocessing(df):
        """
        This function returns a clean dataframe

        :param df:
        :return:
        """
        try:

            col_list = UserPdfParser.return_columns(df)
            col_to_be_chk = [i for i in col_list if not i.isnumeric()
                             and 'Unnamed' not in i
                             and not i.isalpha()
                             and "." not in i]
            if len(col_to_be_chk) == 1:
                col1 = col_to_be_chk[0].split(" ")[0]
                col2 = col_to_be_chk[0].split(" ")[1]
                new = df[col_to_be_chk[0]].str.split(" ", n=1, expand=True)
                df[col_to_be_chk[0]] = new[0]
                df['Unnamed: 3'] = new[1]
                col_list_dot = [i for i in col_list if "." in i]
                column_dict = {
                                    col_to_be_chk[0]: col1,
                                   'Unnamed: 3': col2,
                                   'Unnamed: 4': '',
                                    col_list_dot[0]: col_list_dot[0].split(".")[0]
                              }
                df = UserPdfParser.rename_column(df, column_dict)
                msg = 200
            else:
                msg = u"Sorry we do not support this " \
                      u"format for Now! We are " \
                      u"working on it to provide you a better solution. " \
                      u"Thank you for using our site!"
            return msg, df
        except Exception as e:
            UserPdfParser.logger.error(str(e))

    @staticmethod
    def rename_column(df, col_json):
        """
        This function change the name of dataframe.

        :param df:
        :param col_json:
        :return:
        """
        try:
            df.rename(columns=col_json, inplace=True)
            return df
        except Exception as e:
            UserPdfParser.logger.error(str(e))

    @staticmethod
    def return_columns(df):
        """
        This function returns a list of columns of dataframe

        :param df:
        :return:
        """
        try:
            return df.columns
        except Exception as e:
            UserPdfParser.logger.error(str(e))

    @classmethod
    def create_csv_file(cls, export_path, df):
        """
        This function create a csv file to local storage

        :param export_path
        :param df
        :return:
        """
        try:
            df.to_csv(export_path)
        except Exception as e:
            UserPdfParser.logger.error(str(e))

    @classmethod
    def table_dec(cls, pdf_path, export_csv_path):
        """
        This is a main funtion

        :param pdf_path:
        :param export_csv_path:
        :return:
        """
        try:
            df = cls.read_pdf_to_df(pdf_path)
            msg, df = cls.data_preprocessing(df)
            cls.create_csv_file(export_csv_path, df)
            return df, msg
        except Exception as e:
            UserPdfParser.logger.error(str(e))
