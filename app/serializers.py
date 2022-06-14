from rest_framework import serializers
from .models import BlogModel
class BlogSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = BlogModel
        fields =['title','content','created_at','user_name']
        
    def get_user_name(self, obj):
        return obj.user.username
    
    