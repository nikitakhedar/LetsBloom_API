# Generated by Django 4.2.6 on 2023-12-06 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=500)),
                ('book_container', models.IntegerField()),
                ('registered', models.BooleanField(default=False)),
                ('reg_under', models.IntegerField()),
            ],
        ),
    ]
