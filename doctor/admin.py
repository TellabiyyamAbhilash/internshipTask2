from django.contrib import admin

# Register your models here.
from doctor.models import User,Doctor,Patient,Category,Blog

admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Category)
admin.site.register(Blog)
