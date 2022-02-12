# Generated by Django 2.2 on 2022-02-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250, unique=True)),
                ('last_name', models.CharField(max_length=250, unique=True)),
                ('user_name', models.TextField()),
                ('email', models.TextField()),
                ('password1', models.TextField()),
                ('password2', models.TextField()),
            ],
        ),
    ]
