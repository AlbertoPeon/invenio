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
from invenio.filemanager_helper import create_path_upload, get_cache_key

"""FileManager cut action Plugin"""

class FileAction(object):
  """docstring for Visualizer"""
  name = 'cut'
  
  def action(self, params):
    """
    Cut a CSV file from its different columns
    """
    name = get_cache_key(params)
    original_file = params.get('file')
    fields = params.getlist('field')
    if not original_file or not fields or len(fields) < 2:
    	raise Exception('At least two fields needed!')

    header = urllib2.urlopen(urllib.unquote(original_file)).readline()
    columns_to_remove = [pos for pos, elem in enumerate(header.split(',')) 
    						if elem not in fields]

    import csv
    with open(create_path_upload(name), 'w') as csvfile:
    	csvwriter = csv.writer(csvfile, delimiter=',')
    	csvreader = csv.reader(urllib2.urlopen(urllib.unquote(original_file)))
    	for line in csvreader:
    		csvwriter.writerow([elem for pos, elem in enumerate(line) 
    								if not pos in columns_to_remove])
    		
   	return name
    