# Generated by Django 3.1.1 on 2020-09-17 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_mgmt_sys', '0007_auto_20200916_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorpenname',
            name='pen_name',
            field=models.CharField(default=0, max_length=55),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('roll', models.IntegerField()),
                ('booked', models.ManyToManyField(to='lib_mgmt_sys.Books')),
            ],
        ),
    ]
