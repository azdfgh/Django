# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechacreacion', models.DateTimeField(auto_now_add=True)),
                ('autor', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
                ('identrada', models.ForeignKey(to='blog.Entrada')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
