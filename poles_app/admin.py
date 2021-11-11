from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(AnswerVariant)
admin.site.register(Answer)
