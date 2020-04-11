"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "April 11 16:14:21 2020"
__copyright__ = "©2020 rahul_kumar"

"""

from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    """
    This function validate the valid extension

    :param value:
    :return:
    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Please upload a pdf!')


def validate_year(value):
    """
    This function check the valid extension

    :param value:
    :return:
    """
    if str(value).isnumeric() and len(str(value)) == 4 and value > 1980 and value < 2021:
        pass
    else:
        raise ValidationError('invalid year!')
