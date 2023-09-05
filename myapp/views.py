from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Fields
from .serializers import FieldsSerializer

@api_view(['POST'])
def input_view(request, my_target_field):
    # Verificar si my_target_field es un campo válido
    valid_fields = ["field_1", "author", "description"]
    if my_target_field not in valid_fields:
        return Response({"error": f"{my_target_field} no es un campo válido para convertir a mayúscula"}, status=status.HTTP_400_BAD_REQUEST)

    # Obtener y procesar el JSON de la solicitud
    data = request.data.copy()
    data[my_target_field] = data[my_target_field].upper()

    # Serializar y guardar el objeto en la base de datos
    serializer = FieldsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"id": serializer.data['id']}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_data_view(request, id):
    try:
        item = Fields.objects.get(id=id)
    except Fields.DoesNotExist:
        return Response({"error": "Campo no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = FieldsSerializer(item)
    return Response(serializer.data)


@api_view(['GET'])
def get_all_data_view(request):
    try:
        item = Fields.objects.all()
    except Fields.DoesNotExist:
        return Response({"error": "No hay ningun valor guardado"}, status=status.HTTP_404_NOT_FOUND)

    serializer = FieldsSerializer(item,  many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_field_by_id(request, id):
    try:
        item = Fields.objects.get(id=id)
        item.delete()
        response_data = {
            "message": "El campo se ha eliminado correctamente",
            "id": id  
        }
        serializer = FieldsSerializer(response_data) 
    except Fields.DoesNotExist:
        return Response({"error": "No se pudo eliminar"}, status=status.HTTP_404_NOT_FOUND)
    return Response(response_data)