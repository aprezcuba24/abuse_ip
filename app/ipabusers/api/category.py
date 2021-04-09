from app.utils.paginator import Paginator
from app.ipabusers.api.serializers.category import CategorySerializer
from app.ipabusers.models.category import Category
from rest_framework.viewsets import ReadOnlyModelViewSet


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.order_by("name")
    serializer_class = CategorySerializer
    pagination_class = Paginator
    permission_classes = []
