from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authtoken.views import ObtainAuthToken

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        token = self.get_token(self.user)
        return {
            'refresh': str(token),
            'access': str(token.access_token),
        }

class MyObtainAuthToken(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer