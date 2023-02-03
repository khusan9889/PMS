# Generated by Django 4.1.6 on 2023-02-03 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_projects_options'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name_plural': 'Tasks'},
        ),
        migrations.AddField(
            model_name='tasks',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('in process', 'In_process'), ('test', 'Test'), ('done', 'Done'), ('inactive', 'Inactive')], default='active', max_length=255),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='project_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.projects'),
        ),
    ]