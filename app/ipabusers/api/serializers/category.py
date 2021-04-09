from app.ipabusers.models.category import Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        read_only_fields = ["id", "created_at", "updated_at"]
        fields = ["id", "created_at", "updated_at", "name", "description", "code"]
