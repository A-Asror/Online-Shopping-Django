# Generated by Django 3.2.3 on 2021-06-02 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210602_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='brand',
            field=models.ManyToManyField(blank=True, to='mainapp.Brand'),
        ),
    ]
