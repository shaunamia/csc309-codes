# Generated by Django 4.1.2 on 2022-10-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0006_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
