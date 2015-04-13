from django.contrib import admin
from .models import *

admin.site.register(Comment)
admin.site.register(Notice)
admin.site.register(Category)
admin.site.register(Author)