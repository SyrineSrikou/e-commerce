# Generated by Django 3.2 on 2021-04-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_store_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='logo',
            field=models.ImageField(blank=True, upload_to='stores/logos/'),
        ),
    ]
