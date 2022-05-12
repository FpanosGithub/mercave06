from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from mercave.models import Composicion
from api.serializers import ComposicionSerializer, MoverComposicionSerializer
from mercave.logistica_ferroviaria import mover_composicion

# Create your views here.

@api_view(['GET','POST'])
def lista_composiciones(request):
    if request.method == 'GET':
        composiciones = Composicion.objects.all()
        serializer = ComposicionSerializer(composiciones, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ComposicionSerializer(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_composiciones(request, pk):
    try:
        composicion = Composicion.objects.get(pk=pk)
    except Composicion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ComposicionSerializer(composicion)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ComposicionSerializer(composicion, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        composicion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def mover_composiciones(request, pk):
    if request.method == 'GET':
        composicion = Composicion.objects.get(pk=pk)
        serializer = MoverComposicionSerializer(composicion)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MoverComposicionSerializer(data = request.data)
        if serializer.is_valid():
            lng = request.data['lng']
            lat = request.data['lat']
            destino = {'lng': lng, 'lat': lat}
            composicion = Composicion.objects.get(pk=pk)
            mover_composicion(composicion, destino)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
