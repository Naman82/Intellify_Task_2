from django.contrib import admin
from app.models import User,Student,Teacher

# Models are registered here
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)

