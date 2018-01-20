from django.db import models

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
    published_status = models.CharField(max_length=50, choices=PUBLISHED_CHOICES, default=PUBLISHED_CHOICES[0])
    #author_f - current user as a foreign key
    #author_c - current user as a CharField

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Recipes'
        ordering = ('modified_on',)
