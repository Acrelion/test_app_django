from django.db import models
from django.conf import settings

# Create your models here.
class Recipes(models.Model):
    """
    Recipes class for storing basic recipes.
    """

    PUBLISHED_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )

    title = models.CharField(max_length=160)
    description = models.TextField(max_length=2000, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    published_status = models.CharField(max_length=50, choices=PUBLISHED_CHOICES,
                                        default=PUBLISHED_CHOICES[0])
    #author_f - current user as a foreign key
    #author_c - current user as a CharField
    author_f = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                 null=True, blank=True)

    def __str__(self):
        return self.title

    """
    We can define custom methods
        ( Example: Get number of ingredients via ingredients_set.count() )
    and return it.
    We need to add a short description to the method.
    So if the method is named: get_num_ingredients, the short description
    should be gives as:
    get_num_ingredients.short_description = "Ingredients Count"
    Note: Don't forget to add it to the list_display @ admin.
    """

    class Meta:
        verbose_name_plural = 'Recipes'
        ordering = ('modified_on',)
