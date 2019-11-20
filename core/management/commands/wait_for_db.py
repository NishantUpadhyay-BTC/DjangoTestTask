#!/usr/bin/env python

import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Waiting for the DB to come up
    """

    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB to come up ...")
        time.sleep(3)

        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("DB not up yet, waiting 1 sec ...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("DB is up!!!"))
