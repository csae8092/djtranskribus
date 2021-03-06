# generated by appcreator
from django.db.models import Q
from dal import autocomplete
from . models import *


class TrpCollectionAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = TrpCollection.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(name__icontains=self.q)
            )
        return qs


class TrpDocumentAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = TrpDocument.objects.all()

        if self.q:
            qs = qs.filter(
                Q(title__icontains=self.q) |
                Q(id__icontains=self.q)
            )
        return qs


class TrpPageAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = TrpPage.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(id__icontains=self.q)
            )
        return qs


class TrpTranscriptAC(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = TrpTranscript.objects.all()

        if self.q:
            qs = qs.filter(
                Q(legacy_id__icontains=self.q) |
                Q(id__icontains=self.q)
            )
        return qs
