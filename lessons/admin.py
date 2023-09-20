from django.contrib import admin
from .models import Lesson, Product, Progress

# Register your models here.
admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Progress)
