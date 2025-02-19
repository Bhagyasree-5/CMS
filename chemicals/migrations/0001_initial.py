# Generated by Django 5.0.6 on 2024-06-10 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemicals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chem_name', models.CharField(max_length=100, unique=True)),
                ('Purchased_date', models.DateField(blank=True, null=True)),
                ('Rate', models.IntegerField(blank=True, null=True)),
                ('Quantity_purchased', models.IntegerField(blank=True, null=True)),
                ('Quantity_issued', models.IntegerField(blank=True, null=True)),
                ('Issued_to_whom', models.CharField(max_length=100)),
            ],
        ),
    ]
