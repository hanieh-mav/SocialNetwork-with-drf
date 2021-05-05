from rest_framework import serializers
from posts.models import Post , Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','image','user','description','publish','status','like','created','updated')
        extra_kwargs = {
            'user': {
                'read_only':True
            },
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

