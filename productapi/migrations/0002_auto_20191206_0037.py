# Generated by Django 2.2 on 2019-12-05 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='attribute',
        ),
        migrations.AddField(
            model_name='price',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='price',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
