# Generated by Django 4.2.6 on 2024-07-06 06:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chemicals', '0002_fine_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='UtensilsStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_date', models.DateField(default=django.utils.timezone.now, null=True)),
                ('rate', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('utensil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemicals.utensils')),
            ],
        ),
    ]
