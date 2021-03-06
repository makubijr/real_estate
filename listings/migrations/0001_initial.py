# Generated by Django 4.0.5 on 2022-06-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('num_rooms', models.IntegerField()),
                ('num_beds', models.IntegerField()),
                ('square_foot', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
