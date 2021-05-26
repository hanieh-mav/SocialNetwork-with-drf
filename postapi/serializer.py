from rest_framework import serializers
from posts.models import Post , Comment 
from django.contrib.auth import get_user_model


class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username','first_name','last_name','email','avatar','bio',)



class PostSerializer(serializers.ModelSerializer):
    user = UserSerilaizer()
    class Meta:
        model = Post
        fields = ('id','image','user','description','publish','status','like','created','updated')
        extra_kwargs = {
    
            'publish': {
                'read_only':True
            },
            'created': {
                'read_only':True
            },
            'updated': {
                'read_only':True
            },
            'like': {
                'read_only':True
            },
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','user','reply','post','is_reply','body')
        extra_kwargs = {
            'user':{
                'read_only':True
            },
            'reply':{
                'read_only':True
            },
            'post':{
                'read_only':True
            },
            'is_reply':{
                'read_only':True
            },

        }


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','like')
        extra_kwargs = {
            'like': {
                'read_only':True
            },
        }
