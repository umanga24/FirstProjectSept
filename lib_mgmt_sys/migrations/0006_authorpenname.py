# Generated by Django 3.1.1 on 2020-09-16 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib_mgmt_sys', '0003_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorPenName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='lib_mgmt_sys.author')),
            ],
        ),
    ]
