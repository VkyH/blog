from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogModel(models.Model):
    
    title=models.CharField(max_length=100,blank=False)
    content=models.TextField(max_length=500,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='blogs',default=None)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['-created_at']