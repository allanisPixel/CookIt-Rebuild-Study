from .models import Receita
from . import models
from django_filters.rest_framework import FilterSet
import django_filters
# Rest
from rest_framework import viewsets
from rest_framework import viewsets
from receita.serializers import ( ReceitaSerializer, IngredienteSerializer, 
                                AvaliacaoSerializer, UserSerializer,
                                PostReceitaSerializer )
                                
class ReceitaFilter(FilterSet):
    ingredientes_not = django_filters.BaseInFilter(field_name='ingredientes__nome_ingrediente', lookup_expr='in', exclude=True)
    
    class Meta:
        model = Receita
        fields = {
            'nome_receita': ['icontains'],
            'sabor_receita': ['in'],
            'dificuldade': ['exact'],
            'categoria': ['in'],
            'ingredientes__nome_ingrediente': ['in'],
        }

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = models.Receita.objects.all()
    serializer_class = ReceitaSerializer
    filterset_class = ReceitaFilter

class PostReceitaViewSet(viewsets.ModelViewSet):
    serializer_class = PostReceitaSerializer
    queryset = models.Receita.objects.all()

class IngredienteViewSet(viewsets.ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = models.Ingrediente.objects.all()

class AvaliacaoViewSet(viewsets.ModelViewSet):
    serializer_class = AvaliacaoSerializer
    queryset = models.Avaliacao.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = models.User.objects.all()