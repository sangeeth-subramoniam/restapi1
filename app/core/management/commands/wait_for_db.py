import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django commad to pause the execution until the database is available"""

    def handle(self, *args, **options):
        self.stdout.write('waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('DB Unavailable, Waiting for 1 Second ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available !'))
