from django.contrib import admin
from django.urls import path, include

from core import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'categoria-viewset', viewset=views.CategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categorias/', views.CategoriaView.as_view()),
    path('categorias/<int:id>', views.CategoriaView.as_view()),
    path('categorias-apiview/', views.CategoriaList.as_view()),
    path('categoria-detail-apiview/<int:id>', views.CategoriaDetail.as_view()),
    path('categoria-generic-list-create/', views.CategoriaListGenericAPIView.as_view()),
    path('categoria-generic-retrieve-update-destroy/<int:id>', views.CategoriaDetailGenericAPIView.as_view()),
    path('', include(router.urls))
]
