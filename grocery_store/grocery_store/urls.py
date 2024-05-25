from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from categories.views import CategoriesViewSet, SubCategoriesViewSet
from products.views import ProductsViewSet, BasketViewSet
from users.views import CustomUserViewSet

router = DefaultRouter()

router.register('categories', CategoriesViewSet)
router.register('sub_categories', SubCategoriesViewSet)
router.register('products', ProductsViewSet)
router.register('basket', BasketViewSet)
router.register('user', CustomUserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]
