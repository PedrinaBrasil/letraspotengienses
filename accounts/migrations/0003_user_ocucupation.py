# Generated by Django 3.2.3 on 2021-05-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210525_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ocucupation',
            field=models.CharField(choices=[('Estudante', 'Estudante'), ('Profissional', 'Profissional'), ('Outro', 'Outro')], default='Estudante', max_length=12),
        ),
    ]
