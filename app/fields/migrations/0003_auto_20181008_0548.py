# Generated by Django 2.1.2 on 2018-10-08 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fields', '0002_auto_20181008_0547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='age3',
            new_name='age',
        ),
    ]
