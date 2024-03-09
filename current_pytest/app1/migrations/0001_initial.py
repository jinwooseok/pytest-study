# Generated by Django 5.0.3 on 2024-03-09 11:07

import django.db.models.deletion
import hashid_field.field
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('code', models.CharField(max_length=3, unique=True)),
                ('symbol', models.CharField(default='$', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-.:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c', min_length=8, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(max_length=21)),
                ('payment_intent_id', models.CharField(default=None, max_length=100, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('currency', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app1.currency')),
            ],
        ),
    ]
