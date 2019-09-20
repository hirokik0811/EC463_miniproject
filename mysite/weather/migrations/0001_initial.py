# Generated by Django 2.2.5 on 2019-09-20 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('parent_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]
