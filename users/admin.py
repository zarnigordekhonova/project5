from django.contrib import admin
from users.models import user_info1, user_subscription_info

# Register your models here.
admin.site.register(user_info1)
admin.site.register(user_subscription_info)