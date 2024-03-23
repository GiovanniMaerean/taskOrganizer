# Generated by Django 5.0.3 on 2024-03-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasksOrganizerApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='finalDate',
            new_name='endingDate',
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('3', 'Low'), ('2', 'Medium'), ('1', 'High')], default='2', max_length=1),
        ),
    ]