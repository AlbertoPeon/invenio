# -*- coding: utf-8 -*-
#
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
## 59 Temple Place, Suite 330, Boston, MA 02D111-1307, USA.

"""
WebSession database models.
"""

# General imports.
from invenio.sqlalchemyutils import db
from invenio.websession_model import User
# Create your models here.

class VslConfig(db.Model):
	""" Represents a Visualization config record"""

	__tablename__ = 'VslConfig'
	id = db.Column(db.Integer(15, unsigned=True), primary_key=True,
                   autoincrement=True)
	title = db.Column(db.String(255), nullable=False,
                  server_default='', index=True)
	id_creator = db.Column(db.Integer(15, unsigned=True),
				           db.ForeignKey(User.id), nullable=True)
	graph_type = db.Column(db.String(255), nullable=False,
                     server_default='', index=True)
	config = db.Column(db.Text)

	creator = db.relationship(User, backref='visualization_configs')
"""
	@property
	def json_config(self):
		import json
		return json.loads(self.config)

	@property
	def type(self):
		import json
		return self.json_config.get('type', 'grid')

	@property
	def dataset(self):
		import json
		return self.json_config.get('dataset', {})
"""