# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-12 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0041_auto_20180212_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomer',
            name='replace_sensitive_sso_username',
            field=models.BooleanField(default=False, help_text='Specifies whether to replace the display of potentially sensitive SSO usernames with a more generic name, e.g. EnterpriseLearner.'),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomer',
            name='replace_sensitive_sso_username',
            field=models.BooleanField(default=False, help_text='Specifies whether to replace the display of potentially sensitive SSO usernames with a more generic name, e.g. EnterpriseLearner.'),
        ),
    ]
