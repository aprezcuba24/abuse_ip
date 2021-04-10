from app.ipabusers.api.serializers.ip_category import IpCategoryReadSerializer
from app.ipabusers.models.ipabusers import IpAbusers
from rest_framework import serializers


class IpAbuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAbusers
        read_only_fields = ["id", "created_at", "updated_at", "categories"]
        fields = ["id", "ip", "categories", "created_at", "updated_at"]

    categories = IpCategoryReadSerializer(many=True)
