# generated by appcreator
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,  Layout, Fieldset, Div, MultiField, HTML
from crispy_forms.bootstrap import Accordion, AccordionGroup

from vocabs.models import SkosConcept
from . models import (
    TrpCollection,
    TrpDocument,
    TrpPage,
    TrpTranscript
)


class TrpCollectionFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TrpCollectionFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
                    'id',
                    'name',
                    'description',
                    'page_id',
                    'image_url',
                    'thumb_url',
                    'nr_of_documents',
                    'role',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class TrpCollectionForm(forms.ModelForm):

    class Meta:
        model = TrpCollection
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TrpCollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TrpDocumentFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TrpDocumentFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
                    'id',
                    'title',
                    'author',
                    'upload_time_stamp',
                    'created_at',
                    'genre',
                    'writer',
                    'script_type',
                    'uploader',
                    'uploader_id',
                    'nr_of_pages',
                    'page_id',
                    'image_url',
                    'thumb_url',
                    'external_id',
                    'authority',
                    'description',
                    'language',
                    'status',
                    'created_from_timestamp',
                    'created_to_timestamp',
                    'orig_doc_id',
                    'col_list',
                    'nr_of_regions',
                    'nr_of_transcribed_regions',
                    'nr_of_words_in_regions',
                    'nr_of_lines',
                    'nr_of_words_in_lines',
                    'nr_of_words',
                    'nr_of_transcribed_words',
                    'nr_of_new',
                    'nr_of_in_progress',
                    'nr_of_done',
                    'nr_of_final',
                    'nr_of_gt',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class TrpDocumentForm(forms.ModelForm):

    class Meta:
        model = TrpDocument
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TrpDocumentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TrpPageFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TrpPageFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
                    'id',
                    'part_of',
                    'page_nr',
                    'page_key',
                    'image_id',
                    'page_url',
                    'thum_url',
                    'img_file_name',
                    'width',
                    'height',
                    'created',
                    'indexed',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class TrpPageForm(forms.ModelForm):

    class Meta:
        model = TrpPage
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TrpPageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)


class TrpTranscriptFilterFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(TrpTranscriptFilterFormHelper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_class = 'genericFilterForm'
        self.form_method = 'GET'
        self.helper.form_tag = False
        self.add_input(Submit('Filter', 'Search'))
        self.layout = Layout(
            Fieldset(
                'Basic search options',
                'id',
                css_id="basic_search_fields"
                ),
            Accordion(
                AccordionGroup(
                    'Advanced search',
                    
                    'id',
                    'following',
                    'transcript_key',
                    'part_of',
                    'part_of_document',
                    'transcript_url',
                    'status',
                    'transcriber',
                    'transcriber_id',
                    'timestamp',
                    'nr_of_regions',
                    'nr_of_transcribed_regions',
                    'nr_of_words_in_regions',
                    'nr_of_lines',
                    'nr_of_words_in_lines',
                    'nr_of_words',
                    'gt_id',
                    css_id="more"
                    ),
                AccordionGroup(
                    'admin',
                    'legacy_id',
                    css_id="admin_search"
                    ),
                )
            )


class TrpTranscriptForm(forms.ModelForm):

    class Meta:
        model = TrpTranscript
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TrpTranscriptForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'
        self.helper.add_input(Submit('submit', 'save'),)

