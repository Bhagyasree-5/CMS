# Generated by Django 4.2.6 on 2024-07-06 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0003_utensilsstock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utensils',
            name='uten_id',
        ),
    ]
