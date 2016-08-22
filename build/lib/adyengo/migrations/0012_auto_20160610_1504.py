# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-10 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adyengo', '0011_auto_20160608_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('directdebit_NL', 'Direct Debit (Netherlands)'), ('amex', 'Amex'), ('bankTransfer_DE', 'German Banktransfer'), ('elv', 'ELV'), ('card', 'All debit and credit cards'), ('directEbanking', 'SofortUberweisung'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('visa', 'Visa'), ('ideal', 'iDEAL'), ('paypal', 'PayPal'), ('mc', 'Master Card'), ('bankTransfer', 'All banktransfers')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='recurringpaymentresult',
            name='result_code',
            field=models.CharField(choices=[('Error', 'Error'), ('Authorised', 'Authorised'), ('Received', 'Received'), ('Refused', 'Refused')], max_length=30),
        ),
        migrations.AlterField(
            model_name='session',
            name='country_code',
            field=models.CharField(choices=[('BE', 'Belgium'), ('GB', 'United Kingdom'), ('DE', 'Germany'), ('NL', 'Netherlands')], max_length=2),
        ),
        migrations.AlterField(
            model_name='session',
            name='page_type',
            field=models.CharField(choices=[('multiple', 'Multiple'), ('skip', 'Skip'), ('single', 'Single')], default='multiple', max_length=15),
        ),
        migrations.AlterField(
            model_name='session',
            name='recurring_contract',
            field=models.CharField(blank=True, choices=[('RECURRING,ONECLICK', 'Recurring and One click (user chooses)'), ('ONECLICK', 'One click'), ('RECURRING', 'Recurring')], max_length=50),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_type',
            field=models.CharField(choices=[('api_recurring', 'API Recurring'), ('hpp_regular', 'HPP Regular'), ('hpp_recurring', 'HPP Recurring')], max_length=25),
        ),
        migrations.AlterField(
            model_name='session',
            name='shopper_locale',
            field=models.CharField(blank=True, choices=[('en_GB', 'English (United Kingdom)'), ('de_DE', 'German (Germany)'), ('nl_BE', 'Dutch (Belgium)'), ('fr_BE', 'French (Belgium)'), ('nl_NL', 'Dutch (Holland)')], default='nl_NL', max_length=5),
        ),
        migrations.AlterField(
            model_name='sessionallowedpaymentmethods',
            name='method',
            field=models.CharField(choices=[('directdebit_NL', 'Direct Debit (Netherlands)'), ('amex', 'Amex'), ('bankTransfer_DE', 'German Banktransfer'), ('elv', 'ELV'), ('card', 'All debit and credit cards'), ('directEbanking', 'SofortUberweisung'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('visa', 'Visa'), ('ideal', 'iDEAL'), ('paypal', 'PayPal'), ('mc', 'Master Card'), ('bankTransfer', 'All banktransfers')], max_length=50),
        ),
        migrations.AlterField(
            model_name='sessionblockedpaymentmethods',
            name='method',
            field=models.CharField(choices=[('directdebit_NL', 'Direct Debit (Netherlands)'), ('amex', 'Amex'), ('bankTransfer_DE', 'German Banktransfer'), ('elv', 'ELV'), ('card', 'All debit and credit cards'), ('directEbanking', 'SofortUberweisung'), ('bankTransfer_NL', 'Dutch Banktransfer'), ('visa', 'Visa'), ('ideal', 'iDEAL'), ('paypal', 'PayPal'), ('mc', 'Master Card'), ('bankTransfer', 'All banktransfers')], max_length=50),
        ),
    ]
