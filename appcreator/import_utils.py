import glob
import json

from django.core.serializers.json import DjangoJSONEncoder

from django.apps import apps
from django.conf import settings
from django.core.exceptions import FieldDoesNotExist

from pandas import pandas as pd
from . populate_fields import *


def field_mapping(some_class):
    """ returns a dictionary mapping model field names to lookukp values
        :param some_class: Any django model class with extra field properties
        :return: A dict mapping model field names to lookukp values
    """
    field_mapping_dict = {}
    for x in some_class._meta.get_fields():
        try:
            field_mapping_dict[(x.extra['data_lookup'])] = x.name
        except Exception as e:
            pass
    return field_mapping_dict


def field_mapping_inverse(some_class):
    """ returns a dictionary mapping model field names to lookukp values
        :param some_class: Any django model class with extra field properties
        :return: A dict mapping model field names to lookukp values
    """
    field_mapping_dict = {}
    for x in some_class._meta.get_fields():
        try:
            field_mapping_dict[x.name] = x.extra['data_lookup'].lower().strip()
        except Exception as e:
            pass
    return field_mapping_dict


def fetch_models(app_name):
    """ returns all models from an app
        :param app_name: The name of the application you'd like to recieve the models from
        :return: A list of the app's model classes {app}.models.{ModelName}
    """
    all_models = [x for x in apps.all_models[app_name].values() if '_' not in x.__name__]
    return all_models


def create_file_class_map(app_name, format_string, glob_pattern):
    """ create a dictionary mapping model names to their spreadsheets
        (the spreadsheet must contain the model name)
        :param app_name: The name of the app you'd like to work with
        :format string: A python format string with one placeholder for the actual class name
        :glob_pattern: A python glob pattern matching the files you'd like to import data from
        :return: A dict where class names are keys and the full path to their matching files
    """
    all_models = fetch_models(app_name)
    files = glob.glob(glob_pattern)
    file_class_map = {}
    for cl in all_models:
        for file in files:
            con_file_name = format_string.format(cl.__name__).lower()
            if con_file_name in file.lower():
                file_class_map[cl.__name__] = file
    return file_class_map


def get_class_sources_map(app_name):
    """ create a dictionary mapping model names to their data source tables
        :param app_name: The name of the app you'd like to work with
        :return: A dict where class names are keys and the full path to their matching source tables
    """
    file_class_map = {}
    for x in fetch_models(app_name):
        if x.get_source_table() is not None:
            file_class_map[x.__name__] = x.get_source_table()
    return file_class_map


def delete_all(app_name):
    """ deletes all objects from passed in app
        :param app_name: the app to delte all model class objects from
    """
    print(app_name)
    all_models = fetch_models(app_name)
    print(all_models)
    for x in all_models:
        for y in x.objects.all():
            y.delete()
