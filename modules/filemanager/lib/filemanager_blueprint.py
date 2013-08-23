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

"""FileManager Flask Blueprint"""

from flask import g, request, flash, redirect, url_for, \
    current_app, abort, jsonify, send_from_directory
from invenio.webinterface_handler_flask_utils import _, InvenioBlueprint
from werkzeug.utils import secure_filename
from invenio.filemanager_config import CFG_UPLOAD_FILEMANAGER_FOLDER
from invenio.filemanager_helper import allowed_file, create_path_upload
from invenio.record_blueprint import request_record
from invenio.importutils import autodiscover_modules
import os, urllib, urllib2


blueprint = InvenioBlueprint('filemanager', __name__,
                             url_prefix="/file",
                             #config='invenio.webcomment_config',
                             breadcrumbs=[(_('Visualizations'),
                                           'webvisualize.index')],
                             menubuilder=[('personalize.comment_subscriptions',
                                           _('Your comment subscriptions'),
                                           'webvisualize.index', 20)])

_ACTIONS = dict(map(lambda f: (f.FileAction.name, f.FileAction),
                        autodiscover_modules(['invenio'], related_name_re=".+_fileaction\.py")))

@blueprint.route('/', methods=['GET'])
def index():
    action_name = request.args.get('action')
    newfile = request.args.get('name')
    if action_name and newfile and allowed_file(newfile): 
        _ACTIONS[action_name]().action(newfile=newfile, params=request.args)
        return redirect(url_for('filemanager.uploaded_file', filename=newfile))
    return jsonify(request.args) # change to abort(XXX)

@blueprint.route('/uploads/<path:filename>', methods=['GET'])
def uploaded_file(filename):
    if not allowed_file(filename):
        abort(404)
    return send_from_directory(CFG_UPLOAD_FILEMANAGER_FOLDER, filename)

@blueprint.route('/upload', methods=['GET'])
def upload():
    if not request.args.get('file') or not request.args.get('name') \
            or not allowed_file(request.args['name']):
        abort(404)
    url = urllib2.urlopen(urllib.unquote(request.args['file']))
    filename = secure_filename(request.args['name'])
    with open(create_path_upload(filename), 'w') as file_url:
        file_url.write(url.read())
    return redirect(url_for('filemanager.uploaded_file', filename=filename))
