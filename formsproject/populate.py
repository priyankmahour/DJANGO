import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","formsproject.settings")
import django
django.setup()

from basic_app.models import *
from random import *
from faker import Faker

fakegen = Faker()

def populate(n):
    for i in range(n):
       fname = fakegen.name()
       fmarks= fakegen.random_element(elements=(99,35,58,98,45,75,86,36,25,87))

       record = Student.objects.get_or_create(name=fname,marks=fmarks)

if __name__ =='__main__':
    print("populating Script")
    populate(20)
    print("Script populated....")
