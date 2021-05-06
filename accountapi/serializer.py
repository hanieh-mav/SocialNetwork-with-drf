from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username','first_name','last_name','email','password','avatar','bio')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style': {'input_type': 'password'}
            }
        }

    
    def create(self,validated_data):
        user = get_user_model().objects.create_user(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            password = validated_data['password'],
            avatar = validated_data['avatar'],
            bio = validated_data['bio'],
            )
        return user


    def update(self,instance,validated_data):

        if 'password' in validated_data:

            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance,validated_data)


    