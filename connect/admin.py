from django.contrib import admin
from .models import Foundation, Awareness, Forums, Profile, Comment,Assessment

# Register your models here.
admin.site.register(Foundation)
admin.site.register(Awareness)
admin.site.register(Forums)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Assessment)