# Generated by Django 2.0.1 on 2018-01-20 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_recipes_author_f'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='author_f',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
