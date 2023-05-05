from django.contrib import admin
from cms_app .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Like)