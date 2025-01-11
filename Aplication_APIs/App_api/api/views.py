from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import App
# Create your views here.

@api_view(['POST'])
def add_app(request):
    data = request.data
    app = App.objects.create(
        app_name = data['app_name'],
        version = data['version'],
        description = data['description']
    )
    return Response({'message': 'App added successfully', 
                     'id':app.id}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_app(request, id):
    try:
        app = App.objects.get(id=id)
        return Response({
            'app_name': app.app_name,
            'version': app.version,
            'description': app.description
        })
    except App.DoesNotExist:
        return Response({'error': 'App not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_app(request, id):
    try:
        app = App.objects.get(id=id)
        app.delete()
        return Response({'message': 'App deleted successfully'})
    except App.DoesNotExist:
        return Response({'error': 'App not found'}, status=status.HTTP_404_NOT_FOUND)

