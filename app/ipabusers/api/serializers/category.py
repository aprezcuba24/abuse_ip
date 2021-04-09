from app.ipabusers.models.category import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "created_at", "updated_at", "name", "description", "code"]
