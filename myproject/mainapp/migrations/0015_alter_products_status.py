# Generated by Django 3.2 on 2021-06-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_alter_products_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(default='None', help_text='sale or new', max_length=70),
        ),
    ]