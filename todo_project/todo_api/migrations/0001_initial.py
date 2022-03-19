# Generated by Django 4.0.3 on 2022-03-19 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'todos',
                'verbose_name_plural': 'todos',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
                ('todos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks_ids', to='todo_api.todos')),
            ],
            options={
                'verbose_name': 'task',
                'verbose_name_plural': 'tasks',
                'ordering': ('task',),
            },
        ),
    ]