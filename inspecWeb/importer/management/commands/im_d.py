# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from importer.parser import ConvImporter


class Command(BaseCommand):

    """This class is used for populate the database."""

    def handle(self, *args, **options):
        """This method is used for create objects based in parser."""

        parser = ConvImporter()
        parser.import_data(400)
