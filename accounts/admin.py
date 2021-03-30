from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(contactus)

admin.site.register(TransferredSubscription)
admin.site.register(Subsriber)
admin.site.register(Officer)
admin.site.register(Office)
admin.site.register(OrganizationMember)
admin.site.register(Organization)
