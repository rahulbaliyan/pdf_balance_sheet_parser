userparser Django Application(Django version 2.2)
====


Building
=========


Requirements:
======================
python 3.7

To run this project at your env please follow the steps:
=======================================================
Note:- Recommended OS is linux
1.Go to in project dir
2.Create a virtual env or conda env at your system to install packages(It will not effect your whole system env.)
3.Install requirements.txt for installation dependency packages($ pip install -r requirements.txt)
4.see the .env file and set the logpath, logpath is required to maintain errors and information.
And in this project i am using sqlite db, I added mysql also in settings.py file so can use that one also, please see the .env file and set the db credentials(if you are using mysql or any database.)
5. Run the command ($ python manage.py makemigrations parserapp) to be create schema of the application models.
6. Run the command ($ python manage.py migrate parserapp) to be chnages in database

Api Urls:
=================================
1./pdf_parser/   (this url uses for upload a pdf balance sheet and process the pdf parser engine)
2./download_csv/  (download_csv file)


Licensing
========
*****