from receita.models import Receita, Ingrediente, Avaliacao
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
#    receita = ReceitasSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'
    depth = 1


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class ReceitaSerializer(serializers.ModelSerializer):
#    dono_receita = serializers.SlugRelatedField(
#        many=False,
#        read_only=True,
#        slug_field='first_name'
#    )
    dono_receita = UserSerializer(many=False)
    ingredientes = IngredienteSerializer(many=True)
    class Meta:
        model = Receita
        fields = '__all__'

class PostReceitaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True)
    class Meta:
        model = Receita
        fields = '__all__'
    #=========================================================

    def update(self, instance, validated_data):
        ingredientes_data = validated_data.pop('ingredientes')
        ingredientes = (instance.ingredientes).all()
        ingredientes = list(ingredientes)
        instance.nome_receita = validated_data.get('nome_receita', instance.nome_receita)
        instance.modo_preparo = validated_data.get('modo_preparo', instance.modo_preparo)
        instance.porcoes = validated_data.get('porcoes', instance.porcoes)
        instance.sabor_receita = validated_data.get('sabor_receita', instance.sabor_receita)
        instance.tempo_preparo = validated_data.get('tempo_preparo', instance.tempo_preparo)
        instance.tempo_unidade_medida = validated_data.get('tempo_unidade_medida', instance.tempo_unidade_medida)
        instance.dono_receita = validated_data.get('dono_receita', instance.dono_receita)
        instance.fotos = validated_data.get('fotos', instance.fotos)
        instance.categoria = validated_data.get('categoria', instance.categoria)
        instance.dificuldade = validated_data.get('dificuldade', instance.dificuldade)
        instance.data_publicacao = validated_data.get('data_publicacao', instance.data_publicacao)
        instance.observacoes_adicionais = validated_data.get('observacoes_adicionais', instance.observacoes_adicionais) 
        instance.save()
        #receita = Receita.objects.get(**validated_data)
        
        '''
        for ingrediente in ingredientes_data:
            i=ingredientes.pop(0)
            i.nome_ingrediente = ingrediente.get('nome_ingrediente', ingrediente.nome_ingrediente)
            i.quantidade_ingrediente = ingrediente.get('quantidade_ingrediente', ingrediente.quantidade_ingrediente)
            i.unidade_medida_ingrediente = ingrediente.get('unidade_medida_ingrediente', ingrediente.unidade_medida_ingrediente)
            i.save()
            #a = Ingrediente.objects.create(**ingrediente)
            #i.append(a.id)
        '''

        #receita.ingredientes.set(tuple(i))
        i = []

        for ingrediente in ingredientes_data:
            a = Ingrediente.objects.create(**ingrediente)
            i.append(a.id)
        
        instance.ingredientes.set(tuple(i))

        return instance
    
    #=========================================================
    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes')
        receita = Receita.objects.create(**validated_data)
        i = []

        for ingrediente in ingredientes_data:
            a = Ingrediente.objects.create(**ingrediente)
            i.append(a.id)
        
        receita.ingredientes.set(tuple(i))
        return receita

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'