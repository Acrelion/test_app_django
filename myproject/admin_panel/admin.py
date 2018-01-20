from django.contrib import admin
from admin_panel.models import Recipes

def publish_recipes(modeladmin, request, queryset):
    rows_updated = queryset.update(published_status=Recipes.PUBLISHED_CHOICES[1][0])
    if rows_updated == 1:
        message_bit = "1 recipe was"
    else:
        message_bit = "{} recipes were".format(rows_updated)
    modeladmin.message_user(request, "{} successfully published".format(message_bit))

publish_recipes.short_description = 'Publish Recipes'


# Register your models here.
class RecipesAdmin(admin.ModelAdmin):
    """
    Additional modifications to the model presentation in the admin panel.
    """
    search_fields = ['title', 'description']
    list_display = ['title', 'published_status']
    list_filter = ['published_status']
    actions = [publish_recipes]



admin.site.register(Recipes, RecipesAdmin)
