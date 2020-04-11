from django.db import models
from django.utils import timezone
from parserapp.validators import validate_file_extension, validate_year
# Create your models here.


class BalanceSheet(models.Model):
    year = models.IntegerField(validators=[validate_year])
    query_var = models.CharField(blank=True, null=True, max_length=200)
    file = models.FileField(upload_to='pdf/', validators=[validate_file_extension])
    pdf_uploaded_date = models.DateTimeField(auto_now_add=timezone.now())


# class BalanceSheetCsv(models.Model):
#     pdf = models.ForeignKey(BalanceSheet, on_delete=models.CASCADE, verbose_name="pdf")
#     query_ans = models.CharField(max_length=200)
#     csv = models.FileField(upload_to='csv/')
#     csv_created_date = models.DateTimeField(auto_now_add=timezone.now())