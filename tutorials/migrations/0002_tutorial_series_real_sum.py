# Generated by Django 3.1.5 on 2021-02-03 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial_series',
            name='real_sum',
            field=models.TextField(null=True),
        ),
    ]
