# Generated by Django 5.1.5 on 2025-01-31 04:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('movies', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.order')),
            ],
        ),
    ]
