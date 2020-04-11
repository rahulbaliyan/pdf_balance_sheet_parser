"""
__author__ = "Rahul kumar"
__version__ ="1.0"
__date__ = "April 11 11:14:21 2020"
__copyright__ = "©2020 rahul_kumar"

"""

import logging
import os
from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from parserapp.pdf_parser import UserPdfParser
from parserapp.forms import PdfForms
from parserapp.query import BalanceSheetQuery

logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name='dispatch')
class PdfParser(View):
    def post(self, request):
        form =None
        try:
            form = PdfForms(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                file_name = str(form.cleaned_data['file'])
                pdf_path_path = os.path.join(settings.MEDIA_ROOT, 'pdf/' + file_name)
                csv_file = str(os.path.basename(pdf_path_path).split(".pdf")[0]) + ".csv"
                csv_path = os.path.join(settings.MEDIA_ROOT, 'csv/' + csv_file)
                df, msg = UserPdfParser.table_dec(pdf_path_path, csv_path)
                var = form.cleaned_data["query_var"]
                year = form.cleaned_data["year"]
                if msg != 200:
                    return render(request, "parserapp/pdf_parser_form.html", {'form': form, "msg": df})
                else:
                    resp = BalanceSheetQuery.find_var(var, year, df)
                    resp_json = {"message": resp, "path": csv_file}
            else:
                return render(request, "parserapp/pdf_parser_form.html", {'form': form})
        except Exception as e:
            logger.error(str(e))
            return render(request, "parserapp/pdf_parser_form.html", {'form': form, "msg": "Failed! Try Later!"})
        return render(request, "parserapp/csv_download.html", resp_json)

    def get(self, request):
        form = PdfForms()
        return render(request, "parserapp/pdf_parser_form.html", {'form': form})


class DownloadCsvView(View):
    def get(self, request):
        try:
            file_name = request.GET["path"]
            path = 'csv/' + file_name
            file_path = os.path.join(settings.MEDIA_ROOT, path)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
                    return response
        except Exception as e:
            logger.error(str(e))
        raise Http404