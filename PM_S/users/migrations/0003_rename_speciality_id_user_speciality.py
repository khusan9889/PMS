# Generated by Django 4.1.6 on 2023-02-03 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='speciality_id',
            new_name='speciality',
        ),
    ]
