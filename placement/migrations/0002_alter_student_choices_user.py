# Generated by Django 4.1.5 on 2023-10-08 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('placement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_choices',
            name='user',
            field=models.ForeignKey(default='asare', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
