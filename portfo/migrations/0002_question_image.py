# Generated by Django 3.1.2 on 2020-10-30 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(default=123456897, upload_to='media'),
            preserve_default=False,
        ),
    ]
