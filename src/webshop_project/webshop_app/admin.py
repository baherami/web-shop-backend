from django.contrib import admin

# Register your models here.
from . import models

# Register your models here.

#register the user profile model
admin.site.register(models.UserProfile)
admin.site.register(models.Item)
admin.site.register(models.Cart)
