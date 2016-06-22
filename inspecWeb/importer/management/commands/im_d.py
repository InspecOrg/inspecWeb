# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from importer.parser import Parser


class Command(BaseCommand):

    """This class is used for populate the database."""

    def handle(self, *args, **options):
        """This method is used for create objects based in parser."""

        parser = Parser()
        parser.import_data()
