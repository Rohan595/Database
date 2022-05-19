from rest_framework import generics
from .serializers import CompaniesSerializers
from .models import Comapany

class CompaniesList(generics.ListAPIView):
    queryset = Comapany.objects.order_by('-created_at').all()
    serializer_class = CompaniesSerializers
