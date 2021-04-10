from app.ipabusers.models.ipabusers import IpAbusers
from app.ipabusers.models.category import Category
from django.contrib import admin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(IpAbusers)
class IpAbuserAdmin(admin.ModelAdmin):
    pass
