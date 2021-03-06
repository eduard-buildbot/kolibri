# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-18 17:19
from __future__ import unicode_literals

from functools import partial

import kolibri.core.fields
import kolibri.utils.time
from django.db import migrations


def convert_datetime_to_datetimetz(apps, schema_editor, model_name=None):
    if model_name:
        Model = apps.get_model("kolibriauth", model_name)
        for model in Model.objects.all():
            model.save()

class Migration(migrations.Migration):

    dependencies = [
        ('kolibriauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceowner',
            name='date_joined',
            field=kolibri.core.fields.DateTimeTzField(default=kolibri.utils.time.local_now, editable=False, verbose_name='date joined'),
        ),
        migrations.RunPython(partial(convert_datetime_to_datetimetz, model_name="DeviceOwner")),
        migrations.AlterField(
            model_name='facilityuser',
            name='date_joined',
            field=kolibri.core.fields.DateTimeTzField(default=kolibri.utils.time.local_now, editable=False, verbose_name='date joined'),
        ),
        migrations.RunPython(partial(convert_datetime_to_datetimetz, model_name="FacilityUser")),
    ]
