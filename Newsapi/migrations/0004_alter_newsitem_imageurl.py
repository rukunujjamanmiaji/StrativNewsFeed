# Generated by Django 3.2.9 on 2021-11-25 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Newsapi', '0003_auto_20211125_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='imageurl',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
