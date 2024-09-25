from django_filters import rest_framework as filters

from .models import Feature, Category


class FeatureFilter(filters.FilterSet):
    class Meta:
        model = Feature
        fields = ['id','name']

class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = ['id','name']