from re import I
from rest_framework.views import APIView
from .serializers import RegistrationSerializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response

User = get_user_model()


class RegistrationView(APIView):
    def post(self, request):
        print(request)
        serializers = RegistrationSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response('Thanks for registration! Please activate your account!', status=201)
        return Response(serializers.errors, status=400)


class ActivationView(APIView):
    def get(self, request, code):
        user = User.objects.filter(activation_code=code).first()
        if user:
            user.is_active = True
            user.save()
            return Response(
                'Your account is activated',
                status=200
            )
        return Response('Invalid activation code', status=400)
