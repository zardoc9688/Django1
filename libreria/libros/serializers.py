from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Libro
        fields = ["id","titulo","descripcion","fecha_pub","fecha_creacion","autor","categoria"]