from rest_framework import serializers
from mercave.models import Composicion, Vagon, Bogie, Eje

class ComposicionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Composicion
        fields = ('id','codigo','descripcion','operador','lng','lat')

class MoverComposicionSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    codigo = serializers.CharField(required = False, max_length= 16)
    lng = serializers.FloatField()
    lat = serializers.FloatField()

