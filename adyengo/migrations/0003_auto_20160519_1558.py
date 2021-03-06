# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-19 13:58
from __future__ import unicode_literals

import adyengo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adyengo', '0002_auto_20160428_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurringpaymentresult',
            name='result_code',
            field=models.CharField(choices=[('Error', 'Error'), ('Authorised', 'Authorised'), ('Refused', 'Refused')], max_length=30),
        ),
        migrations.AlterField(
            model_name='session',
            name='country_code',
            field=models.CharField(blank=True, choices=[('BE', 'Belgium'), ('DE', 'Germany'), ('GB', 'United Kingdom'), ('NL', 'Netherlands')], max_length=2),
        ),
        migrations.AlterField(
            model_name='session',
            name='currency_code',
            field=models.CharField(choices=[('EUR', 'Euro')], default='EUR', max_length=3),
        ),
        migrations.AlterField(
            model_name='session',
            name='page_type',
            field=models.CharField(choices=[('skip', 'Skip'), ('multiple', 'Multiple'), ('single', 'Single')], default='multiple', max_length=15),
        ),
        migrations.AlterField(
            model_name='session',
            name='recurring_contract',
            field=models.CharField(blank=True, choices=[('RECURRING,ONECLICK', 'Recurring and One click (user chooses)'), ('RECURRING', 'Recurring'), ('ONECLICK', 'One click')], max_length=50),
        ),
        migrations.AlterField(
            model_name='session',
            name='res_url',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_type',
            field=models.CharField(choices=[('api_recurring', 'API Recurring'), ('hpp_recurring', 'HPP Recurring'), ('hpp_regular', 'HPP Regular')], max_length=25),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_validity',
            field=models.DateTimeField(default=adyengo.models.tomorrow, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='ship_before_date',
            field=models.DateTimeField(default=adyengo.models.tomorrow, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='shopper_locale',
            field=models.CharField(blank=True, choices=[('fr_BE', 'French (Belgium)'), ('nl_BE', 'Dutch (Belgium)'), ('nl_NL', 'Dutch (Holland)'), ('de_DE', 'German (Germany)'), ('en_GB', 'English (United Kingdom)')], default='nl_NL', max_length=5),
        ),
        migrations.AlterField(
            model_name='sessionallowedpaymentmethods',
            name='method',
            field=models.CharField(choices=[('visa', 'Visa'), ('ideal', 'iDEAL'), ('directEbanking', 'SofortUberweisung'), ('elv', 'ELV'), ('mc', 'Master Card'), ('bankTransfer', 'All banktransfers'), ('amex', 'Amex'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('paypal', 'PayPal'), ('card', 'All debit and credit cards'), ('directdebit_NL', 'Direct Debit (Netherlands)'), ('bankTransfer_DE', 'German Banktransfer')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sessionblockedpaymentmethods',
            name='method',
            field=models.CharField(choices=[('visa', 'Visa'), ('ideal', 'iDEAL'), ('directEbanking', 'SofortUberweisung'), ('elv', 'ELV'), ('mc', 'Master Card'), ('bankTransfer', 'All banktransfers'), ('amex', 'Amex'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('paypal', 'PayPal'), ('card', 'All debit and credit cards'), ('directdebit_NL', 'Direct Debit (Netherlands)'), ('bankTransfer_DE', 'German Banktransfer')], max_length=50),
        ),
    ]
