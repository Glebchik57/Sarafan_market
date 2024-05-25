from rest_framework import viewsets
from django.contrib.auth import get_user_model

from .serializers import CategoriesSerializer, SubCategoriesSerializer
from .models import Categories, SubCategories
from .permissions import IsAdminOrReadOnly


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminOrReadOnly,)


class SubCategoriesViewSet(viewsets.ModelViewSet):
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer
    permission_classes = (IsAdminOrReadOnly,)
