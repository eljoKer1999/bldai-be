# Generated by Django 4.1.2 on 2022-10-30 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bld', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]