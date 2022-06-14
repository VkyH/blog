from django.shortcuts import render,redirect
from .forms import CustomRegistrationForm
from rest_framework.decorators import api_view
from .models import BlogModel
from .serializers import BlogSerializer
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form=CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('login')
    else:        
        register_form=CustomRegistrationForm()
    return render(request, 'register.html',{'register_form':register_form})


@api_view()
def home(request):
    blogs=BlogModel.objects.all()
    serializer=BlogSerializer(blogs,many=True)
    return Response(serializer.data)
    
@login_required
@api_view(['POST'])
def blogpost(request):
    serializer=BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
    return Response(serializer.data)

