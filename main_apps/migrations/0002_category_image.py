# Generated by Django 4.0.3 on 2022-04-06 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=None, upload_to='media/', verbose_name='couvertur'),
            preserve_default=False,
        ),
    ]
