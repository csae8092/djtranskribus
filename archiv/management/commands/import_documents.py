import os
import datetime
import warnings
import logging

from tqdm import tqdm
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from archiv.models import TrpCollection, TrpDocument
from archiv.utils import update_docs


warnings.filterwarnings('ignore')

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Import Documents"

    def handle(self, *args, **kwargs):
        overall_start_time = datetime.datetime.now()
        current_cols = TrpCollection.objects.all()
        current_docs = TrpDocument.objects.all()
        root_logger = logging.getLogger('')
        root_logger.setLevel(logging.INFO)

        logging.info(f"Starting to import Documents for {current_cols.count()} Collections")
        logging.info(f"Current number of Documents: {current_docs.count()}")
        logging.info(f"start import/update at: {overall_start_time}")
        for x in tqdm(current_cols, total=current_cols.count()):
            logging.info(f"importing documents for collection {x}")
            update_docs(x)
        logging.info(f"Documents before: {current_docs.count()}")
        logging.info(f"Documents after: {TrpDocument.objects.all().count()}")
        logging.info(f"finished at {datetime.datetime.now()}")
        return f"done"
