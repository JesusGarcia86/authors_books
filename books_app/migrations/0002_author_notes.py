# Generated by Django 2.2 on 2020-10-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='new_text'),
            preserve_default=False,
        ),
    ]