from .serializers import CartSerializer
from rest_framework import generics
from .models import Cart

# Create your views here.

class CartListView(generics.ListAPIView):
    serializer= CartSerializer
    queryset=Cart.objects.all()