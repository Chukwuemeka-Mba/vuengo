# Generated by Django 3.1.4 on 2022-02-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('todo', 'Todo'), ('done', 'Done')], default='todo', max_length=20)),
            ],
        ),
    ]
