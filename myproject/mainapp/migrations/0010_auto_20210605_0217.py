# Generated by Django 3.2 on 2021-06-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='answer',
            field=models.TextField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='created_add',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
