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
from invenio.filemanager_helper import allowed_file, create_path_upload

"""FileManager join action Plugin"""

class FileAction(object):
  """docstring for Visualizer"""
  name = 'join'
  
  def action(self, newfile, params):
  	"""
  	Merges several csv files in one and it is uploaded to Invenio.
  	Note: All files must have the same header
  	"""
  	files = params.getlist('file')
  	if len(files) < 2:
  		raise Exception('Two o more files needed to join!')

  	# check headers
  	header = urllib2.urlopen(urllib.unquote(files[0])).readline()
  	for i in range(1, len(files)):
  		if urllib2.urlopen(urllib.unquote(files[i])).readline() != header:
  			raise Exception('Different Header!')

  	# joining		
  	with open(create_path_upload(newfile), 'w') as final_file:
  		final_file.write(header)
  		for f in files:
  			url = urllib2.urlopen(f)
  			url.readline() # skip header
  			for line in url.readlines():
  				final_file.write(line)
    			
    