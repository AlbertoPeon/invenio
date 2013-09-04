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
import urllib, urllib2, csv, json

"""FileManager tranform action Plugin"""

class FileAction(object):
    """docstring for Visualizer"""
    name = 'transform'
    
    def _csv_to_json(self, params):
        name = "temp"
        original_file = params.get('file')

        json_file = []
        csvreader = csv.reader(urllib2.urlopen(urllib.unquote(original_file)))
        header = csvreader.next()
        for line in csvreader:
            dict_line = {}
            for index in range(len(line)):
                dict_line[header[index]] = line[index]
            json_file.append(dict_line)
        """
        with open(create_path_upload(name), 'w') as final_file:
            final_file.write(json.dumps(json_file))
        """
        return name


    def _json_to_csv(self, params):
        name = "temp"
        
        return name

    methods = {
                'csv': _json_to_csv,
                'json':_csv_to_json
              }
  
    def action(self, params):
        """
        Transforms a CSV file to a JSON file or the contrary
        """
        to_format = params.get('to')
        original_file = params.get('file')
        
        if (not original_file or not to_format or (to_format != 'csv' 
                                           and to_format != 'json')):
            raise Exception('Wrong params!')
        return self.methods[to_format](self, params)    