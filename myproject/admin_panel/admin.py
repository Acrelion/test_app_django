from django.contrib import admin
from admin_panel.models import Recipes

# Register your models here.
class RecipesAdmin(admin.ModelAdmin):
    """
    Additional modifications to the model presentation in the admin panel.
    """
    search_fields = ['title', 'description']
    list_display = ['title', 'published_status']


admin.site.register(Recipes, RecipesAdmin)
