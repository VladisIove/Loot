# Generated by Django 2.2 on 2019-04-15 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('img', models.ImageField(upload_to='img/')),
                ('size_loot', models.CharField(choices=[('S', 'Маленький подарок'), ('M', 'Большой подарок'), ('B', 'Огромный подарок')], default='S', max_length=1)),
                ('descr', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, default='fast', max_length=120)),
                ('s_name', models.CharField(blank=True, default='fast', max_length=120)),
                ('phone', models.CharField(max_length=13)),
                ('e_mail', models.EmailField(blank=True, default='fast@gmail.com', max_length=120)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('choose', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='serializerLoot.Loots')),
            ],
            options={
                'ordering': ['-data'],
            },
        ),
    ]
