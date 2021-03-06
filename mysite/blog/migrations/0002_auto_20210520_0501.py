# Generated by Django 3.2 on 2021-05-20 05:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('address', models.CharField(max_length=300)),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.school'),
            preserve_default=False,
        ),
    ]
