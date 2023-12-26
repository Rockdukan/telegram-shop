from django.contrib import admin

from .models import *


admin.site.register(TelegramUser)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Order)
