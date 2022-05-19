from .models import Comapany
from rest_framework import serializers


class CompaniesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Comapany
        fields = '__all__'