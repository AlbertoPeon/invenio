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

"""FileManager helper methods"""

from invenio.cache import cache
from invenio.filemanager_config import CFG_UPLOAD_FILEMANAGER_FOLDER, \
									   CFG_UPLOAD_ALLOWED_EXTENSIONS
import os

def create_path_upload(filename):
	if not os.path.exists(CFG_UPLOAD_FILEMANAGER_FOLDER):
  		os.makedirs(CFG_UPLOAD_FILEMANAGER_FOLDER)
  	return os.path.join(CFG_UPLOAD_FILEMANAGER_FOLDER,  filename)

def get_cache_key(params):
	import hashlib
	m = hashlib.md5()
	query = []
	for key in sorted(params.keys()):
		query.append(key)
		query.append(params[key])
	m.update(''.join(query))
	return m.hexdigest()

def cache_file(params, final_file):
	key = get_cache_key(params)
	if not cache.get(key):
		cache.set(key, final_file)
	return cache.get(key)



