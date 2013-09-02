# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.
import urllib, urllib2
from invenio.filemanager_config import CFG_UPLOAD_FILEMANAGER_FOLDER
from invenio.filemanager_helper import create_path_upload

"""FileManager tranform action Plugin"""

class FileAction(object):
  """docstring for Visualizer"""
  name = 'transform'

  def _csv_to_json(filename):
  	pass

  def _json_to_csv(filename):
  	pass 
  
  def action(self, newfile, params):
    """
    Filter a CSV file by a value in its header
    """
    to_format = params.get('to')

    