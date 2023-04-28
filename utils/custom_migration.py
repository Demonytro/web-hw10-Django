import os
import django

os.environ.setdefault("DJANGO_SETTING_MODULE", "hw_project.settings")
django.setup()
print('hello1')
from quotes.models import Quote, Tag, Author
print('hello')