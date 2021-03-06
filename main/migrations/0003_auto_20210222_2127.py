# Generated by Django 3.0 on 2021-02-22 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_remove_folder_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_data_relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.ManyToManyField(to='main.File')),
                ('folders', models.ManyToManyField(to='main.Folder')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User_folder_relation',
        ),
    ]
