# Generated by Django 3.0.4 on 2020-03-16 02:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('snippet', '0005_auto_20200315_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
        ),
    ]
