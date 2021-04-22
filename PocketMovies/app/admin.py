from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Producer)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Profile)
