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
import jinja2

from google.appengine.ext import db

jinja_env = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))


class Handler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_front(self, subject="", content="", error=""):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")
        self.render("post_index.html", subject=subject, content=content, error=error, posts=posts)

    def render_post(self, posts=""):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC")
        self.render("front_index.html", posts=posts)


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class MainPage(Handler):
    def get(self):
        self.render_post()


class NewPostHandler(Handler, Post):

    def get(self):
        t = jinja_env.get_template('post_index.html')
        self.response.out.write(t.render())

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if subject and content:
            a = Post(subject=subject, content=content)
            a.put()
            p_id = a.key().id()
            self.redirect("/blog/%s" % p_id)

        else:
            error = "We need both a subject and come content!"
            self.render_front(subject, content, error=error)


class PermalinkHandler(Handler):
    def get(self, p_id):
        blog_entry = Post.get_by_id(int(p_id))
        self.render("permalink_index.html", blog_entry=blog_entry)

app = webapp2.WSGIApplication([('/blog', MainPage),
                               ('/blog/newpost', NewPostHandler),
                               (r'/blog/(\d+)', PermalinkHandler)],
                              debug=True)
