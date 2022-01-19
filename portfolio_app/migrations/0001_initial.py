# Generated by Django 4.0.1 on 2022-01-16 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'emails',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.email')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.name')),
            ],
            options={
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.AddField(
            model_name='email',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.name'),
        ),
    ]