# Generated by Django 2.2.5 on 2019-11-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20191118_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='this is a description'),
            preserve_default=False,
        ),
    ]