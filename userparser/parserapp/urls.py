"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "April 11 12:14:21 2020"
__copyright__ = "©2020 rahul_kumar"

"""

from django.urls import path
# from django.views.generic import TemplateView
from . import views

urlpatterns = [
        path('pdf_parser/', views.PdfParser.as_view(), name='pdf_parser'),
        path('download_csv/', views.DownloadCsvView.as_view(), name='download_csv'),
        # path('parser_form/', TemplateView.as_view(template_name='parserapp/pdf_parser_form.html')),
    ]