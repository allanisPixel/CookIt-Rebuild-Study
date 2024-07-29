from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Para upload de imagens
from django.conf.urls.static import static  # Para upload de imagens
from rest_framework.routers import DefaultRouter
from receita.views import ( ReceitaViewSet, IngredienteViewSet,
                          AvaliacaoViewSet, UserViewSet,
                          PostReceitaViewSet )

from usuario.views import UsuarioReceitaViewSet

router = DefaultRouter()

router.register('user', UserViewSet, basename='user')
router.register('receita', ReceitaViewSet, basename = 'receita')
router.register('avaliacao', AvaliacaoViewSet, basename = 'avaliacao')
router.register('ingrediente', IngredienteViewSet, basename = 'ingrediente')
router.register('post-receita', PostReceitaViewSet, basename = 'post-receita')

router.register('usuario-receita', UsuarioReceitaViewSet, basename = 'usuario-receita')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls) ),
    path('api/', include('usuario.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
