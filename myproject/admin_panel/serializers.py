from rest_framework import serializers
from admin_panel.models import Recipes

class RecipesSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Recipes model.
    """

    class Meta:
        model = Recipes
        fields = '__all__'
        