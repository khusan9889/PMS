# Generated by Django 4.1.6 on 2023-02-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialities', '0004_alter_specialities_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialities',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
