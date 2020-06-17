from django.conf import settings

from tqdm import tqdm
from transkribus_utils.transkribus_utils import (
    trp_list_collections, trp_list_docs, trp_get_doc_overview_md
)
from appcreator.import_utils import field_mapping

from . models import TrpCollection, TrpDocument, TrpPage

try:
    user = settings.TRANSKRIBUS['user']
except (AttributeError, KeyError) as e:
    print("no TRANSKRIBUS user set in the project's settings file")
    print(e)
    user = "user"

try:
    pw = settings.TRANSKRIBUS['pw']
except (AttributeError, KeyError) as e:
    print("no TRANSKRIBUS pw set in the project's settings file")
    print(e)
    pw = "pw"


def update_collections():
    """ creates TrpCollection objects from all collections of a Transkribus user
        :return: the result of the transkribus-collections-rest-endpoint
    """
    collections_json = trp_list_collections(user, pw)
    field_dict = field_mapping(TrpCollection)
    for x in tqdm(collections_json, total=len(collections_json)):
        item = {}
        for source_key, target_key in field_dict.items():
            target_value = x.get(source_key, None)
            if target_value is not None:
                item[target_key] = target_value
        temp_item, _ = TrpCollection.objects.get_or_create(id=item['id'])
        for cur_attr, my_val in item.items():
            if cur_attr == 'id':
                continue
    #         print(cur_attr, my_val)
            setattr(temp_item, cur_attr, my_val)
            temp_item.save()
    return collections_json


def import_pages(doc, page_list):
    """ create TrpPage objects from TrpDocument
        :param doc: A TrpDocument object
        :param page_list: A dict with page-info (retrieved from Transkribus API)
        :return: a string "done"
    """
    source = page_list
    field_dict = field_mapping(TrpPage)
    print(f"{len(page_list)} Pages to import: ")
    for x in tqdm(page_list, total=len(page_list)):
        p_id = x['pageId']
        temp_item, _ = TrpPage.objects.get_or_create(id=p_id)
        item = {}
        for source_key, target_key in field_dict.items():
            target_value = x.get(source_key, None)
            if target_value is not None:
                item[target_key] = target_value
        temp_item, _ = TrpPage.objects.get_or_create(id=item['id'])
        for cur_attr, my_val in item.items():
            try:
                setattr(temp_item, cur_attr, my_val)
            except ValueError:
                pass
        temp_item.part_of = doc
        temp_item.save()
    return "done"


def update_docs(col):
    """ fetches all documents from collection
        :param col: a TrpCollection object
        :return: the result of the transkribus-docs-rest-endpoint
    """
    source_list = trp_list_docs(col.id, user, pw)
    field_dict = field_mapping(TrpDocument)
    print(f"Collection {col} holds {len(source_list)} Documents ")
    for x in tqdm(source_list, total=len(source_list)):
        item = {}
        for source_key, target_key in field_dict.items():
            target_value = x.get(source_key, None)
            if target_value is not None:
                item[target_key] = target_value
        temp_item, _ = TrpDocument.objects.get_or_create(id=item['id'])
        for cur_attr, my_val in item.items():
            if cur_attr == 'id':
                continue
    #         print(cur_attr, my_val)
            setattr(temp_item, cur_attr, my_val)
            temp_item.col_list.add(col)
        temp_item.save()
    return source_list


def enrich_doc(doc):
    """ writes additional doc-metadata to doc object
        :param doc: a TrpDocument object
        :return: the enriched document
    """
    try:
        col_id = doc.col_list.all()[0].id
    except Exception as e:
        print(f"ERROR: {e}")
        return doc
    item_source = trp_get_doc_overview_md(doc.id, col_id, user, pw)
    md = item_source['trp_return']['md']
    try:
        page_list = item_source["trp_return"]['pageList']['pages']
    except KeyError:
        pages = None
    field_dict = field_mapping(doc.__class__)
    item = {}
    for source_key, target_key in field_dict.items():
        if "__md__" in source_key:
            source_key = source_key.split('__md__')[-1]
            target_value = md.get(source_key, None)
            if target_value is not None:
                item[target_key] = target_value
    for cur_attr, my_val in item.items():
        setattr(doc, cur_attr, my_val)
    doc.save()
    if page_list is not None:
        import_pages(doc, page_list)
    return doc
