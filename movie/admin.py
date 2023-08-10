from django.contrib import admin
from .models import Movie, Trailer, User
from django.contrib.auth.admin import UserAdmin

# Adding the fields to the class UserAdmin
fields = list(UserAdmin.fieldsets)
fields.append(
    ("History",
    {"fields": ("seen_movies",)}
    )
)
UserAdmin.fieldsets = tuple(fields)

# Register your models here.
admin.site.register(Movie)
admin.site.register(Trailer)
admin.site.register(User, UserAdmin)
