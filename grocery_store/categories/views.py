from rest_framework import viewsets

from .serializers import CategoriesSerializer, SubCategoriesSerializer
from .models import Categories, SubCategories
from .permissions import IsAdminOrReadOnly


class CategoriesViewSet(viewsets.ModelViewSet):
    '''Вьюсет для работы с категориями'''
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminOrReadOnly,)


class SubCategoriesViewSet(viewsets.ModelViewSet):
    '''Вьюсет для работы с подкатегориями'''
    queryset = SubCategories.objects.all()
    serializer_class = SubCategoriesSerializer
    permission_classes = (IsAdminOrReadOnly,)
