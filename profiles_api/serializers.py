from rest_framework import serializers

#access this while creating a modelserializer
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        #password should be write only as only new user has to enter new password ,old user shouldnot retrive it
        extra_kwargs = {
            'password': {
            'write_only':True,
            'style':{'input_type': 'password'}
            }

        }
        #override the ModelSerializer so that password will be saved as hash
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
            return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializer profile feed Item"""


    class Meta:
        model = models.ProfileFeedItem
        fields= ('id','user_profile','status_text','created_on')
        extra_kwargs= {'user_profile':{'read_only': True}}
