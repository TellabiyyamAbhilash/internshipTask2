# Generated by Django 4.0.6 on 2022-08-21 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_alter_doctor_firstname_alter_doctor_lastname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('summary', models.TextField()),
                ('content', models.CharField(max_length=250)),
                ('category', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='doctor.category')),
            ],
        ),
    ]