#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aiida.orm import DataFactory
from aiida.parsers.parser import Parser

class SymmetriesParser(Parser):
    """
    Parse output symmetries file.
    """
    def parse_with_retrieved(self, retrieved):
        try:
            out_folder = retrieved[self._calc._get_linkname_retrieved()]
        except KeyError as e:
            self.logger.error("No retrieved folder found")
            raise e

        new_nodes_list = [(
            'symmetries',
            DataFactory('singlefile')(file=out_folder.get_abs_path(
                self._calc._OUTPUT_FILE_NAME
            ))
        )]

        return True, new_nodes_list
