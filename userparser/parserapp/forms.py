from django import forms
from parserapp.models import BalanceSheet


class PdfForms(forms.ModelForm):
    class Meta:
        model = BalanceSheet
        fields = "__all__"


# class CsvForms(forms.ModelForm):
#     class Meta:
#         model = BalanceSheetCsv
#         fields = "__all__"