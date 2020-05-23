from transkribus.trp_utils import trp_list_collections, trp_list_docs, trp_get_doc_md
from appcreator.import_utils import field_mapping

from . models import TrpCollection, TrpDocument


def update_collections():
    """ creates TrpCollection objects from all collections of a Transkribus user
        :return: the result of the transkribus-collections-rest-endpoint
    """
    collections_json = trp_list_collections()
    field_dict = field_mapping(TrpCollection)
    for x in collections_json:
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


def update_docs(col):
    """ fetches all documents from collection
        :param col: a TrpCollection object
        :return: the result of the transkribus-docs-rest-endpoint
    """
    source_list = trp_list_docs(col.id)
    field_dict = field_mapping(TrpDocument)
    for x in source_list:
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
    col_id = doc.col_list.all()[0].id
    item_source = trp_get_doc_md(doc.id, col_id=col_id)
    field_dict = field_mapping(doc.__class__)
    item = {}
    for source_key, target_key in field_dict.items():
        if "__md__" in source_key:
            source_key = source_key.split('__md__')[-1]
            target_value = item_source.get(source_key, None)
            if target_value is not None:
                item[target_key] = target_value
    for cur_attr, my_val in item.items():
        setattr(doc, cur_attr, my_val)
    doc.save()
    return doc
