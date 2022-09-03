from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes


# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    return render(request, "template_ods4_apps/home.html")