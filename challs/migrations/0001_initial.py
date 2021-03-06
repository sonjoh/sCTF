# Generated by Django 4.0 on 2021-12-29 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('points', models.IntegerField(default=1000)),
                ('solves', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=255)),
                ('task', models.CharField(max_length=255)),
            ],
        ),
    ]
