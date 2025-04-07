from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import UserViewSet

from core.views import UserViewSet, CategoriaViewSet, EditoraViewSet, AutorViewSet ,LivroViewSet 

router = DefaultRouter()
router.register(r"autores", AutorViewSet) # nova linha
router.register(r"categorias", CategoriaViewSet) # nova linha
router.register(r"editoras", EditoraViewSet) # nova linha
router.register(r"livros", LivroViewSet) # nova linha
router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]

