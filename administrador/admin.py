from django.contrib import admin
from .models import Administrador, Author, Book, Publisher

# Register your models here.

admin.site.register(Administrador)
admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
