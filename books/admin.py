from django.contrib import admin
from books.models import Books_info, Books_rent_info

# Register your models here.
admin.site.register(Books_info)
admin.site.register(Books_rent_info)