from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Feature
from .serializers import CategorySerializer,FeatureSerializer
from .filters import CategoryFilter,FeatureFilter
# Create your views here.


@api_view(['GET'])
def get_categories(request):
    categories= Category.objects.all()
    filter = CategoryFilter(request.GET, queryset=categories)
    serializer = CategorySerializer(filter.qs, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_features(request):
    features= Feature.objects.all()
    filter = FeatureFilter(request.GET, queryset=features)
    serializer = FeatureSerializer(filter.qs, many=True)

    return Response(serializer.data)