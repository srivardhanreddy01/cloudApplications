from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserAccount
from .serializers import UserAccountSerializer

class UserAccountList(APIView):
    def get(self, request):
        users = UserAccount.objects.all()
        serializer = UserAccountSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
