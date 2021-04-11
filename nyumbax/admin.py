from django.contrib import admin
from .models import Hood, Business, Post, Essential, Location

# Register your models here.
admin.site.register(Hood)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Essential)
admin.site.register(Location)
