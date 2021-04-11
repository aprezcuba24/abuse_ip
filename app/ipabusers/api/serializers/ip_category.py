from app.ipabusers.api.serializers.category import CategorySerializer
from app.ipabusers.models.ipabusers import IpAbusers
from app.ipabusers.models.ip_category import IpCategory
from rest_framework import serializers


class IpCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IpCategory
        read_only_fields = ["id", "reported_by", "created_at", "updated_at"]
        fields = ["id", "ip_address", "category"]

    ip_address = serializers.CharField(required=True, max_length=100)

    def create(self, validated_data):
        ip, _ = IpAbusers.objects.get_or_create(ip=validated_data["ip_address"])
        del validated_data["ip_address"]
        reported_by = validated_data["reported_by"]
        try:
            return IpCategory.objects.get(ip=ip, users=reported_by, category=validated_data["category"])
        except IpCategory.DoesNotExist:
            pass
        validated_data["ip"] = ip
        return super().create(validated_data)


class IpCategoryReadSerializer(IpCategorySerializer):
    category = CategorySerializer()
