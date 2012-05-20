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
import webapp2



welcome = """<h2>Welcome to my Udacity Practice App!</h2>"""

main_html="""
<h3>So far I have completed:</h3>
<ul>
  <li><a href="rot13">Homework 2-1: Rot13</a></li>
  <li><a href="/usersignup">Homework 2-2: User Signup</a></li>
  <li><a href="/asciichan">Asciichan!</a></li>
  <li><a href="/blog">Blog!</a></li>
</ul>"""


class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(welcome)
    self.response.out.write(main_html)


app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)


