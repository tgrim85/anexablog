#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2
import rot13function
import dataValidation
import jinja2

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))



class MainPage(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('rot13_index.html')
    self.response.out.write(template.render())


  def post(self):
    

    userInput = rot13function.rot_13(self.request.get('text'))
    
    template_values = {
        'uinput': userInput
    }

    template = jinja_environment.get_template('rot13_index.html')
    
    self.response.out.write(template.render(template_values))
    

app = webapp2.WSGIApplication([('/rot13', MainPage)],
                              debug=True)


