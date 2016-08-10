from django.contrib import admin
from schoolApp.models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin


admin.site.register(About)
admin.site.register(categories)
admin.site.register(activities)
admin.site.register(Consultation)
admin.site.register(ConsultationSchedule)
admin.site.register(News)
admin.site.register(Gallery)
admin.site.register(Personnel)
