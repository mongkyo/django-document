# Generated by Django 2.1.2 on 2018-10-10 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('many_to_many', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('f', 'Follow'), ('b', 'Block')], max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('relation_users', models.ManyToManyField(through='many_to_many.Relation', to='many_to_many.TwitterUser')),
            ],
        ),
        migrations.AddField(
            model_name='relation',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_by_from_user', to='many_to_many.TwitterUser'),
        ),
        migrations.AddField(
            model_name='relation',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations_by_to_user', to='many_to_many.TwitterUser'),
        ),
    ]
