# Generated by Django 4.1.4 on 2023-01-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_refund'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='display',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
