# Generated by Django 4.1.6 on 2023-02-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project_docs',
            options={'verbose_name_plural': 'Project Docs'},
        ),
        migrations.AlterField(
            model_name='project_docs',
            name='file',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]