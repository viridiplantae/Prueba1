from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from agencia.models import Marca, Auto, Inventario, Ventas
from agencia.serializer import MarcaSerializer, AutoSerializer, InventarioSerializer, VentaSerializer

# Create your views here.
class MarcaViews(APIView):
    """
    Ejemplo:
    {
        "nombre":"Mini"
    }
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            serializer = MarcaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = serializer.data 
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            list_obj = Marca.objects.all()
            serializer = MarcaSerializer(list_obj, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AutoViews(APIView):
    """
    Ejemplo:
    {
        "marca":1,
        "nombre":"Audi A4",
        "color":"plata"
    }
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            serializer = AutoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            list_obj = Auto.objects.all()
            serializer = AutoSerializer(list_obj, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class InventarioViews(APIView):
    """
    Ejemplo:
    {
        "codigo":1,
        "descripcion":"Auto color oro",
        "cantidad":5
    }
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            serializer = InventarioSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            list_obj = Inventario.objects.all()
            serializer = InventarioSerializer(list_obj, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        try:
            serializer = InventarioSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            obj_inventario = Inventario.objects.get(codigo=serializer.data["codigo"])
            obj_inventario.cantidad = obj_inventario.cantidad + serializer.data["cantidad"]
            obj_inventario.save()
            data = {
                'msg':'Se ha actualizado el inventario'
            }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VentasViews(APIView):
    """
    Ejemplo:
    {
        "cod_inventario":2,
        "cantidad_venta":1
    }
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            serializer = VentaSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            id_venta = serializer.data["id"]
            print(id_venta)

            
            cantidad_venta = serializer.data["cantidad_venta"]

            cod_producto = serializer.data["cod_inventario"]

            cantidad_inventario = Inventario.objects.get(id=cod_producto)

            if cantidad_venta <= cantidad_inventario.cantidad:
                cantidad_inventario.cantidad = cantidad_inventario.cantidad - cantidad_venta
                
                status_venta = Ventas.objects.get(id= id_venta)
                status_venta.venta_valida = True
                status_venta.save()
                cantidad_inventario.save()
                
                data = {
                    'msg':'La venta es válida. Se vendieron ' + str(cantidad_venta) + ' autos, quedan ' + str(cantidad_inventario.cantidad)
                }
                
            else:
                data = {
                    'msg':'La venta no es válida'
                }
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            list_obj = Ventas.objects.all()
            serializer = VentaSerializer(list_obj, many= True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)