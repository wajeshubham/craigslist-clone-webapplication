# Generated by Django 3.0.5 on 2020-04-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='searches',
            field=models.CharField(max_length=500, null=True),
        ),
    ]