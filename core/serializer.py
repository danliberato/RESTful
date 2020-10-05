from rest_framework import serializers
from .models import User


########    CUSTOMER    ########
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'document')

