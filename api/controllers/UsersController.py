from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from api.serializers import UserRequest, UserSerializer
from api.services.UsersServices import get, create, update, delete

class UsersController(ViewSet):
    def list(self, request):
        users = get()
        return Response({
            "message": "List of users",
            "data": UserSerializer(users, many=True).data
        })
    
    def retrieve(self, request, pk=None):
        user = get(pk)

        if not user:
            return Response({
                "message": f"User {pk} not found"
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "message": f"Details of user {pk}",
            "data": UserSerializer(user).data
        })
    
    def create(self, request):
        serializer = UserRequest(data=request.data)
        if not serializer.is_valid():
            return Response({
                "message": "Invalid data",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = create(request.data)

        if not user:
            return Response({
                "message": "Failed to create user"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            "message": "User created",
            "data": UserSerializer(user).data
        })
    
    def update(self, request, pk=None):
        serializer = UserRequest(data=request.data)
        if not serializer.is_valid():
            return Response({
                "message": "Invalid data",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = update(pk, request.data)

        if not user:
            return Response({
                "message": f"User {pk} not found or failed to update"
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "message": f"User {pk} updated",
            "data": UserSerializer(user).data
        })
    
    def destroy(self, request, pk=None):
        user = delete(pk)

        if not user:
            return Response({
                "message": f"User {pk} not found or failed to delete"
            }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "message": f"User {pk} deleted",
            "data": UserSerializer(user).data
        })