# Generated by Django 3.2.10 on 2022-07-16 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JAL', '0003_account'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='UserAccount',
        ),
    ]