from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(MyUser)
admin.site.register(MyDoctor)
admin.site.register(Slot)
admin.site.register(ReserveSlot)
