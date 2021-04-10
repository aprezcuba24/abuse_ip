from app.ipabusers.api.serializers.ip_category import IpCategorySerializer
from app.utils.permissions import IsBotPermission
from app.ipabusers.api.serializers.ip_abuser import IpAbuserSerializer
from app.ipabusers.models.ipabusers import IpAbusers
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from app.utils.paginator import Paginator


class IpAbuserViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = IpAbusers.objects.order_by("-created_at")
    serializer_class = IpAbuserSerializer
    pagination_class = Paginator
    permission_classes = [IsBotPermission]
    filterset_fields = ["ip"]

    def get_serializer_class(self):
        return IpCategorySerializer if self.action == "create" else super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)
