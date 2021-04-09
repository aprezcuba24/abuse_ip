from app.ipabusers.models.ipabusers import IpAbusers
from rest_framework import serializers


class IpAbuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpAbusers
        read_only_fields = ["id", "created_at", "updated_at"]
        fields = ["id", "ip"]
