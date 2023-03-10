# Generated by Django 4.1.6 on 2023-02-03 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_projects_options'),
        ('project_docs', '0002_alter_project_docs_options_alter_project_docs_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_docs',
            name='project_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projects'),
        ),
    ]
