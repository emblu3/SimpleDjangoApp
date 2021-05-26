# Generated by Django 3.2 on 2021-05-26 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210520_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=400)),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='school',
            name='address',
        ),
        migrations.RemoveField(
            model_name='school',
            name='zip_code',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_of_resumption',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='graduation_year',
            field=models.IntegerField(default=1, max_length=4),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.faculty')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='certificate_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.certificate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.grade'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.department'),
        ),
    ]