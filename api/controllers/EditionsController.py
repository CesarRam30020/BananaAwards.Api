from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from api.serializers import EditionRequest, EditionSerializer
from api.services.EditionsServices import get, create, update, delete

class EditionsController(ViewSet):
    def list(self, request):
        editions = get()
        return Response({
            "message": "List of editions",
            "data": EditionSerializer(editions, many=True).data
        })

    def retrieve(self, request, pk=None):
        edition = get(pk)

        if not edition:
            return Response({
                "message": f"Edition {pk} not found"
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "message": f"Details of edition {pk}",
            "data": EditionSerializer(edition).data
        })

    def create(self, request):
        serializer = EditionRequest(data=request.data)
        if not serializer.is_valid():
            return Response({
                "message": "Invalid data",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        edition = create(request.data)

        if not edition:
            return Response({
                "message": "Failed to create edition",
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "Edition created",
            "data": EditionSerializer(edition).data
        })

    def update(self, request, pk=None):
        serializer = EditionRequest(data=request.data)
        if not serializer.is_valid():
            return Response({
                "message": "Invalid data",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        edition = update(pk, request.data)

        if not edition:
            return Response({
                "message": f"Edition {pk} not found or failed to update"
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "message": f"Edition {pk} updated",
            "data": EditionSerializer(edition).data
        })
    
    def destroy(self, request, pk=None):
        edition = delete(pk)

        if not edition:
            return Response({
                "message": f"Edition {pk} not found or failed to delete"
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "message": f"Edition {pk} deleted",
            "data": EditionSerializer(edition).data
        })