from app.ipabusers.api.serializers.ip_abuser import IpAbuserSerializer
from app.ipabusers.models.ipabusers import IpAbusers
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from app.utils.paginator import Paginator


class IpAbuserViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = IpAbusers.objects.order_by("-created_at")
    serializer_class = IpAbuserSerializer
    pagination_class = Paginator
    permission_classes = []
