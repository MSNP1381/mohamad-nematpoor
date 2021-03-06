# Generated by Django 3.1.2 on 2020-10-31 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfo', '0002_question_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='porto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='potrfo/image/')),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
