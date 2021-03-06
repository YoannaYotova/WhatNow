# Generated by Django 3.0.6 on 2020-06-01 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UsersType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='UsersTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opened', models.BooleanField(default=False)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Tasks')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='user_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.UsersType'),
        ),
    ]
