import os
import datetime
import warnings
import logging

from tqdm import tqdm
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from archiv.models import TrpCollection
from archiv.utils import update_collections


warnings.filterwarnings('ignore')

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Import/Updates Collection"

    def handle(self, *args, **kwargs):
        overall_start_time = datetime.datetime.now()
        current_col_count = TrpCollection.objects.all().count()
        root_logger = logging.getLogger('')
        root_logger.setLevel(logging.INFO)
        logging.info(f"Collections before: {current_col_count}")
        logging.info(f"start import/update at: {overall_start_time}")
        import_start = update_collections()
        current_col_count = TrpCollection.objects.all().count()
        logging.info(f"Collections before: {current_col_count}")
        logging.info(f"Collections after: {TrpCollection.objects.all().count()}")
        logging.info(f"finished at {datetime.datetime.now()}")
        return f"done"
