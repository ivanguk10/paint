from django.contrib import admin

from .models import Service
from .models import SubService
from .models import Price
from .models import Comment

admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(Price)
admin.site.register(Comment)
