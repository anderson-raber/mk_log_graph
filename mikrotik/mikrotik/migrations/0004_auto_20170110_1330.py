# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-10 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mikrotik', '0003_auto_20170110_1327'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Firewall',
            new_name='Firewall_Info',
        ),
        migrations.RenameModel(
            old_name='FirewallLogin',
            new_name='Firewall_Login',
        ),
        migrations.RenameModel(
            old_name='FirewallLoginError',
            new_name='Firewall_Login_Error',
        ),
    ]
