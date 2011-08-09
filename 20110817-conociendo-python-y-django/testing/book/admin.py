from django.contrib import admin

from book import models as m

admin.site.register(m.Book)
