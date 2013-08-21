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

from datetime import datetime
import socket

from flask import g, render_template, request, flash, redirect, url_for, \
    current_app, abort, jsonify

from invenio.webinterface_handler_flask_utils import _, InvenioBlueprint
from invenio.webuser_flask import current_user

from invenio.sqlalchemyutils import db
from invenio.webvisualize_model import VslConfig
from invenio.webvisualize_forms import AddVisualizationForm
from invenio.webvisualize_model import VslConfig
from invenio.websession_model import User

# TEMPORAL
from invenio.websearch_model import Collection


blueprint = InvenioBlueprint('filemanager', __name__,
                             url_prefix="/file",
                             #config='invenio.webcomment_config',
                             breadcrumbs=[(_('Visualizations'),
                                           'webvisualize.index')],
                             menubuilder=[('personalize.comment_subscriptions',
                                           _('Your comment subscriptions'),
                                           'webvisualize.index', 20)])

from invenio.record_blueprint import request_record


@blueprint.route('/', methods=['GET'])
def index():
    return jsonify({'test':'works!'})
