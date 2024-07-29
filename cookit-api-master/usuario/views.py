from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from receita.serializers import ReceitaSerializer

from receita.models import Receita
from django_filters.rest_framework import FilterSet
from rest_framework import viewsets

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data="Only for Logged in User", status=status.HTTP_200_OK)

class ReceitaFilter(FilterSet):
    class Meta:
        model = Receita
        fields = {
            'dono_receita': ['in'],
        }

class UsuarioReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    filterset_class = ReceitaFilter











