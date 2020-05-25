import os
import datetime
import warnings
import logging

from tqdm import tqdm
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from archiv.models import TrpCollection, TrpDocument, TrpPage
from archiv.utils import enrich_doc


warnings.filterwarnings('ignore')

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Import Pages"

    def handle(self, *args, **kwargs):
        overall_start_time = datetime.datetime.now()
        current_cols = TrpCollection.objects.all()
        current_docs = TrpDocument.objects.all()
        current_pages = TrpPage.objects.all()
        root_logger = logging.getLogger('')
        root_logger.setLevel(logging.INFO)

        logging.info(
            f"Import Pages for {current_docs.count()} Documents in {current_cols.count()} Collections"
        )
        logging.info(f"start import/update at: {overall_start_time}")
        for x in tqdm(current_docs, total=current_docs.count()):
            logging.info(f"importing documents for collection {x}")
            enrich_doc(x)
        logging.info(f"Pages before: {current_pages.count()}")
        logging.info(f"Pages after: {TrpPage.objects.all().count()}")
        logging.info(f"finished at {datetime.datetime.now()}")
        return f"done"
