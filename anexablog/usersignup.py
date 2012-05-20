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
import dataValidation
import jinja2

jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))


class MainPage(webapp2.RequestHandler):
  
  def get(self):
    template = jinja_environment.get_template('signup_index.html') 
    self.response.out.write(template.render())

  def post(self):
    template = jinja_environment.get_template('signup_index.html')

    user_username = self.request.get('username')
    user_password = self.request.get('password')
    user_email = self.request.get('email')
    user_verify= self.request.get("verify")


    username = dataValidation.valid_username(user_username)
    password = dataValidation.valid_password(user_password)
    email = dataValidation.valid_email(user_email)

    verror=""
    uerror=""
    perror=""
    eerror=""

    

    if user_password != user_verify:
      verror = "The passwords do not match!"

    elif not (username and password and user_verify and email):
      if not username:
        uerror = "The username is invalid."
      if not email:
        eerror = "The email is invalid."
      if not password:
        perror = "The password is invalid."

    else:
      self.redirect('/welcome?username=%s' %user_username)

    template_values = {
          'uerror': uerror,
          'perror': perror,
          'verror': verror,
          'eerror': eerror,
          'username': user_username,
          'password': user_password,
          'verify': user_verify,
          'email': user_email
      }

    
    self.response.out.write(template.render(template_values))

class WelcomeHandler(webapp2.RequestHandler):
  def get(self):
    user_username = self.request.get('username')
    self.response.out.write("<h2>Welcome, %s!</h2>" %user_username)
    self.response.out.write("<a href=\"/usersignup\">Back to form</a>")


app = webapp2.WSGIApplication([('/usersignup', MainPage),
                               ('/welcome', WelcomeHandler)],
                              debug=True)


