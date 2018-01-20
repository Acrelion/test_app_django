from rest_framework import generics
from admin_panel.serializers import RecipesSerializer
from admin_panel.models import Recipes


# Create your views here.
"""
class RecipesList(APIView):
    def get(self, request):
        recipes = Recipes.objects.all()
        serializer = RecipesSerializer(recipes, many=True)
        return Response(serializer.data)



    def post(self, request):
        serializer = RecipesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipesDetail(APIView):
    def get_object(self, pk):
        try:
            return Recipes.objects.get(pk=pk)
        except Recipes.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipesSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipesSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""


class RecipesList(generics.ListCreateAPIView):
    """
    View class for Recipes.
    Returns all the recipes on get request.
    Can write down a new recipe on post request.
    URL: recipes/
    """
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer


class RecipesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View class for a single recipe.
    Controls the get/put(update)/delete single recipe.
    Creation of a recipe is defined in the RecipeList class.
    """
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
