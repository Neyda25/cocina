# Generated by Django 3.0.7 on 2020-09-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='imagen',
            field=models.ImageField(blank='True', null='True', upload_to='post/'),
            preserve_default='True',
        ),
    ]