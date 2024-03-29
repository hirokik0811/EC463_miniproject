# Generated by Django 2.2.5 on 2019-09-20 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('parent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
            options={
                'verbose_name_plural': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='TempHumidData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField(verbose_name=0)),
                ('parent_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='temperature.Room')),
                ('parent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
            options={
                'verbose_name_plural': 'datas',
            },
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.IntegerField()),
                ('parent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
            options={
                'verbose_name_plural': 'intervals',
            },
        ),
    ]
