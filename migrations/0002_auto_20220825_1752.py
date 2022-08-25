# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-08-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loc_deposit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journalsrn',
            options={'verbose_name': 'Journal SRN', 'verbose_name_plural': 'Journal SRNs'},
        ),
        migrations.AddField(
            model_name='journalsrn',
            name='journal_name_filename',
            field=models.CharField(default='dummy_journal_title', help_text='Slug-field like name of the journal to be added to the filename eg. a_demo_journal', max_length=255),
            preserve_default=False,
        ),
    ]
