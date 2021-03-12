# Generated by Django 3.1.7 on 2021-03-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('whatsapp_no', models.CharField(max_length=15)),
                ('year', models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Pre-Final'), ('4', 'Final'), ('5', 'Alumni')], max_length=6)),
                ('branch', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('Bowler', 'Bowler'), ('Batsman', 'Batsman'), ('Allrounder', 'Allrounder'), ('Keeper', 'Keeper')], max_length=20)),
                ('block', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=6)),
                ('room_number', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]