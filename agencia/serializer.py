from rest_framework import serializers
from agencia.models import Marca, Auto, Inventario, Ventas

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MarcaSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Marca
        fields = [
            'id',
            'nombre',
        ]


class AutoSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Auto
        fields = [
            'id',
            'marca',
            'nombre',
            'color',
        ]


class InventarioSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Inventario
        fields = [ 
            'id',
            'codigo',
            'descripcion',
            'cantidad'
        ]


class VentaSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Ventas
        fields = [ 
            'id',
            'cod_inventario',
            'cantidad_venta',
            'venta_valida'
        ]