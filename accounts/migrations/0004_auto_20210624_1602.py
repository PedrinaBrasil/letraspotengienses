# Generated by Django 3.2.3 on 2021-06-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_ocucupation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='ocucupation',
            field=models.CharField(choices=[('Estudante', 'Estudante'), ('Profissional', 'Profissional'), ('Outro', 'Outro')], default='Estudante', max_length=12, verbose_name='Ocupação'),
        ),
    ]
