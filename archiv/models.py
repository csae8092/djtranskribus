# generated by appcreator

from django.contrib.gis.db import models
from django.urls import reverse


from browsing.browsing_utils import model_to_dict


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class IdProvider(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    legacy_id = models.CharField(
        blank=True, null=True,
        max_length=250,
    )

    class Meta:
        abstract = True


class TrpCollection(IdProvider):
    """ A collection of documents """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    id = models.BigIntegerField(
        primary_key=True,
        verbose_name="ID",
        help_text="Collection ID",
    ).set_extra(
        is_public=True,
        data_lookup="colId",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="Collection ID <value>",
    )
    name = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Name",
        help_text="Collection Name",
    ).set_extra(
        is_public=True,
        data_lookup="colName",
        arche_prop="hasTitle",
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name="Description",
        help_text="A brief description of the collection ",
    ).set_extra(
        is_public=True,
        data_lookup="description",
        arche_prop="hasDescription",
    )
    page_id = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Page ID",
        help_text="Page ID",
    ).set_extra(
        is_public=True,
        data_lookup="pageId",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="Page ID <value>",
    )
    image_url = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Image URL",
        help_text="Image URL",
    ).set_extra(
        is_public=True,
        data_lookup="url",
    )
    thumb_url = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Thumb URL",
        help_text="Thumb URL",
    ).set_extra(
        is_public=True,
        data_lookup="thumbUrl",
    )
    nr_of_documents = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Number of Documents",
        help_text="Number of Documents",
    ).set_extra(
        is_public=True,
        data_lookup="nrOfDocuments",
        arche_prop="hasExtent",
        arche_prop_str_template="<value> Documents",
    )
    role = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Role",
        help_text="Role",
    ).set_extra(
        is_public=True,
        data_lookup="role",
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
        ).set_extra(
            is_public=True
        )

    class Meta:

        ordering = [
            'name',
        ]
        verbose_name = "Collection"

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:trpcollection_browse')

    @classmethod
    def get_source_table(self):
        return "https://transkribus.eu/TrpServer/rest/collections/list"


    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:trpcollection_create')

    def get_absolute_url(self):
        return reverse('archiv:trpcollection_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('archiv:trpcollection_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:trpcollection_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:trpcollection_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:trpcollection_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:trpcollection_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class TrpDocument(IdProvider):
    """ A Transkribus Document """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    id = models.BigIntegerField(
        primary_key=True,
        verbose_name="ID",
        help_text="Document ID",
    ).set_extra(
        is_public=True,
        data_lookup="docId",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="Document ID <value>",
    )
    title = models.TextField(
        blank=True, null=True,
        verbose_name="Title",
        help_text="Document Title",
    ).set_extra(
        is_public=True,
        data_lookup="title",
        arche_prop="hasTitle",
    )
    author = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Author",
        help_text="Author of the Document",
    ).set_extra(
        is_public=True,
        data_lookup="author",
        arche_prop="hasDescription",
        arche_prop_str_template="Author of the Document <value>",
    )
    upload_time_stamp = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Upload Timestamp",
        help_text="Upload Timestamp",
    ).set_extra(
        is_public=True,
        data_lookup="uploadTimestamp",
    )
    created_at = models.DateField(
        blank=True, null=True,
        verbose_name="Creation Time",
        help_text="Creation Time of the Document",
    ).set_extra(
        is_public=True,
        arche_prop="hasCollectedStartDate",
    )
    genre = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Genre",
        help_text="Genre",
    ).set_extra(
        is_public=True,
        data_lookup="genre",
        arche_prop="hasDescription",
        arche_prop_str_template="Genre: <value>",
    )
    writer = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Writer",
        help_text="Writer/Hand",
    ).set_extra(
        is_public=True,
        data_lookup="writer",
        arche_prop="hasDescription",
        arche_prop_str_template="Writer/Hand: <value>",
    )
    script_type = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Script Type",
        help_text="Script Type",
    ).set_extra(
        is_public=True,
        data_lookup="scriptType",
        arche_prop="hasDescription",
        arche_prop_str_template="Script type: <value>",
    )
    uploader = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Uploader (email)",
        help_text="Uploader Email",
    ).set_extra(
        is_public=False,
        data_lookup="uploader",
    )
    uploader_id = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Uploader (ID)",
        help_text="Uploader ID",
    ).set_extra(
        is_public=False,
        data_lookup="uploaderId",
    )
    nr_of_pages = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Number of Pages",
        help_text="Number of Pages",
    ).set_extra(
        is_public=True,
        data_lookup="nrOfPages",
        arche_prop="hasExtent",
        arche_prop_str_template="<value> pages",
    )
    page_id = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Page ID",
        help_text="Page ID",
    ).set_extra(
        is_public=True,
        data_lookup="pageId",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="Page ID <value>",
    )
    image_url = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Image URL",
        help_text="Image URL",
    ).set_extra(
        is_public=True,
        data_lookup="url",
    )
    thumb_url = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Thumb URL",
        help_text="Thumb URL",
    ).set_extra(
        is_public=True,
        data_lookup="thumbUrl",
    )
    external_id = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="External ID",
        help_text="External ID",
    ).set_extra(
        is_public=True,
        data_lookup="externalId",
        arche_prop="hasIdentifier",
    )
    authority = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Authority",
        help_text="Authority",
    ).set_extra(
        is_public=True,
        data_lookup="authority",
        arche_prop="hasDescription",
        arche_prop_str_template="Authority: <value>",
    )
    description = models.TextField(
        blank=True, null=True,
        verbose_name="Description",
        help_text="Description",
    ).set_extra(
        is_public=True,
        data_lookup="desc",
        arche_prop="hasDescription",
    )
    language = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Language",
        help_text="Language of the Document",
    ).set_extra(
        is_public=True,
        data_lookup="language",
        arche_prop="hasLanguage",
    )
    status = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Status",
        help_text="Status",
    ).set_extra(
        is_public=True,
        data_lookup="status",
    )
    created_from_timestamp = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Created (start)",
        help_text="Created (start)",
    ).set_extra(
        is_public=True,
        data_lookup="createdFromTimestamp",
    )
    created_to_timestamp = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Created (end)",
        help_text="Created (end)",
    ).set_extra(
        is_public=True,
        data_lookup="createdToTimestamp",
    )
    orig_doc_id = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="origDocId",
        help_text="origDocId",
    ).set_extra(
        is_public=True,
        data_lookup="origDocId",
        arche_prop="hasAlter",
    )
    col_list = models.ManyToManyField(
        "TrpCollection",
        related_name='rvn_trpdocument_col_list_trpcollection',
        blank=True,
        verbose_name="Part of Collection(s)",
        help_text="Part of Collection(s)",
    ).set_extra(
        is_public=True,
        data_lookup="colList__colId",
        arche_prop="isPartOf",
    )
    nr_of_regions = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfRegions",
        help_text="nrOfRegions",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfRegions",
    )
    nr_of_transcribed_regions = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfTranscribedRegions",
        help_text="nrOfTranscribedRegions",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfTranscribedRegions",
    )
    nr_of_words_in_regions = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfWordsInRegions",
        help_text="nrOfWordsInRegions",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfWordsInRegions",
    )
    nr_of_lines = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfLines",
        help_text="nrOfLines",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfLines",
    )
    nr_of_words_in_lines = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfWordsInLines",
        help_text="nrOfWordsInLines",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfWordsInLines",
    )
    nr_of_words = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfWords",
        help_text="nrOfWords",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfWords",
    )
    nr_of_transcribed_words = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfTranscribedWords",
        help_text="nrOfTranscribedWords",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfTranscribedWords",
    )
    nr_of_new = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfNew",
        help_text="nrOfNew",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfNew",
    )
    nr_of_in_progress = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfInProgress",
        help_text="nrOfInProgress",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfInProgress",
    )
    nr_of_done = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfDone",
        help_text="nrOfDone",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfDone",
    )
    nr_of_final = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfFinal",
        help_text="nrOfFinal",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfFinal",
    )
    nr_of_gt = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfGT",
        help_text="nrOfGT",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__md__nrOfGT",
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
        ).set_extra(
            is_public=True
        )

    class Meta:

        ordering = [
            'id',
        ]
        verbose_name = "Document"

    def __str__(self):
        if self.id:
            return "{}".format(self.id)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:trpdocument_browse')

    @classmethod
    def get_source_table(self):
        return "https://transkribus.eu/TrpServer/rest/collections/{col_id}/list"


    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:trpdocument_create')

    def get_absolute_url(self):
        return reverse('archiv:trpdocument_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('archiv:trpdocument_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:trpdocument_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:trpdocument_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:trpdocument_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:trpdocument_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class TrpPage(IdProvider):
    """ A Transkribus Page """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    id = models.BigIntegerField(
        primary_key=True,
        verbose_name="Page ID",
        help_text="Page ID",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__pageId",
    )
    part_of = models.ForeignKey(
        "TrpDocument",
        related_name='rvn_trppage_part_of_trpdocument',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="part of Document",
        help_text="part of Document",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__docId",
    )
    page_nr = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Page Number",
        help_text="Page Number",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__pageNr",
    )
    page_key = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Key of the Page",
        help_text="Key of the Page",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__key",
        arche_prop_str_template="hasNonLinkedIdentifier",
    )
    image_id = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="ID of Image",
        help_text="ID of Image",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__imageId",
        arche_prop_str_template="hasNonLinkedIdentifier",
    )
    page_url = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="URL of Image",
        help_text="URL of Image",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__url",
    )
    thum_url = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Thumb URL",
        help_text="Thumb URL",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__thumbUrl",
    )
    img_file_name = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Filename",
        help_text="Filename",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__imgFileName",
    )
    width = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="width",
        help_text="width",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__width",
        arche_prop_str_template="hasExtent",
    )
    height = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="height",
        help_text="height",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__height",
        arche_prop_str_template="hasExtent",
    )
    created = models.DateField(
        blank=True, null=True,
        verbose_name="created",
        help_text="created",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__created",
        arche_prop_str_template="hasCreatedDate",
    )
    indexed = models.BooleanField(
        default=False,
        blank=True, null=True,
        verbose_name="indexed",
        help_text="indexed",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__pageList__pages__indexed",
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
        ).set_extra(
            is_public=True
        )

    class Meta:

        ordering = [
            'id',
        ]
        verbose_name = "Page"

    def __str__(self):
        if self.id:
            return "{}".format(self.id)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:trppage_browse')

    @classmethod
    def get_source_table(self):
        return "https://transkribus.eu/TrpServer/rest/collections/{col_id}/{doc_id}/fulldoc"


    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:trppage_create')

    def get_absolute_url(self):
        return reverse('archiv:trppage_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('archiv:trppage_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:trppage_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:trppage_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:trppage_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:trppage_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


class TrpTranscript(IdProvider):
    """ A Transkribus Transcript """
    legacy_id = models.CharField(
        max_length=300, blank=True,
        verbose_name="Legacy ID"
        )
    id = models.BigIntegerField(
        primary_key=True,
        verbose_name="Transcript ID",
        help_text="Transcript ID",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__tsId",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="Collection ID: <value>",
    )
    following = models.ForeignKey(
        "TrpTranscript",
        related_name='rvn_trptranscript_following_trptranscript',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="follows",
        help_text="follows",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__parentTsId",
    )
    transcript_key = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Key of Transcript",
        help_text="Key of Transcript",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__key",
        arche_prop="hasNonLinkedIdentifier",
        arche_prop_str_template="Transcript Key: <value>",
    )
    part_of = models.ForeignKey(
        "TrpPage",
        related_name='rvn_trptranscript_part_of_trppage',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Transcript of Page",
        help_text="Transcript of Page",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__pageId",
        arche_prop="isPartOf",
    )
    part_of_document = models.ForeignKey(
        "TrpDocument",
        related_name='rvn_trptranscript_part_of_document_trpdocument',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Part of Document",
        help_text="Part of Document",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__docId",
    )
    transcript_url = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Url of Transcript",
        help_text="Url of Transcript",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__url",
    )
    status = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="status",
        help_text="status",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__status",
    )
    transcriber = models.CharField(
        blank=True, null=True,
        max_length=250,
        verbose_name="Transcriber (email)",
        help_text="Transcriber (email)",
    ).set_extra(
        is_public=False,
        data_lookup="fulldoc__tsList__transcripts__userName",
    )
    transcriber_id = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Transcriber (ID)",
        help_text="Transcriber (ID)",
    ).set_extra(
        is_public=False,
        data_lookup="fulldoc__tsList__transcripts__userId",
    )
    timestamp = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="Timestamp",
        help_text="Timestamp",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__userId",
    )
    nr_of_regions = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfRegions",
        help_text="nrOfRegions",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__nrOfRegions",
    )
    nr_of_transcribed_regions = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfTranscribedRegions",
        help_text="nrOfTranscribedRegions",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__nrOfTranscribedRegions",
    )
    nr_of_words_in_regions = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfWordsInRegions",
        help_text="nrOfWordsInRegions",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__nrOfWordsInRegions",
    )
    nr_of_lines = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfLines",
        help_text="nrOfLines",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__nrOfLines",
    )
    nr_of_words_in_lines = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfWordsInLines",
        help_text="nrOfWordsInLines",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__nrOfWordsInLines",
    )
    nr_of_words = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="nrOfWords",
        help_text="nrOfWords",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__nrOfWords",
    )
    gt_id = models.BigIntegerField(
        blank=True, null=True,
        verbose_name="gtId",
        help_text="gtId",
    ).set_extra(
        is_public=True,
        data_lookup="fulldoc__tsList__transcripts__gtId",
    )
    orig_data_csv = models.TextField(
        blank=True,
        null=True,
        verbose_name="The original data"
        ).set_extra(
            is_public=True
        )

    class Meta:

        ordering = [
            'id',
        ]
        verbose_name = "Transcript"

    def __str__(self):
        if self.id:
            return "{}".format(self.id)
        else:
            return "{}".format(self.legacy_id)

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('archiv:trptranscript_browse')

    @classmethod
    def get_source_table(self):
        return "https://transkribus.eu/TrpServer/rest/collections/{col_id}/{doc_id}/fulldoc"


    @classmethod
    def get_natural_primary_key(self):
        return "id"

    @classmethod
    def get_createview_url(self):
        return reverse('archiv:trptranscript_create')

    def get_absolute_url(self):
        return reverse('archiv:trptranscript_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('archiv:trptranscript_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('archiv:trptranscript_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('archiv:trptranscript_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'archiv:trptranscript_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'archiv:trptranscript_detail',
                kwargs={'pk': prev.first().id}
            )
        return False
