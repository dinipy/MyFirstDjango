from django.contrib import admin

# Register your models here.
from dini.models import Person , Employer, Login, Register
admin.site.register(Person)
admin.site.register(Employer)
admin.site.register(Login)
admin.site.register(Register)