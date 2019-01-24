# Generated by Django 2.0.2 on 2019-01-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bisonMatchApp', '0003_auto_20190122_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMatches',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('studentlnumber', models.CharField(db_column='StudentLNumber', max_length=255)),
                ('matchlnumber', models.CharField(db_column='MatchLNumber', max_length=255)),
            ],
            options={
                'db_table': 'StudentMatches',
                'managed': True,
            },
        ),
    ]
