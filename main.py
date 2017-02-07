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
import caesar
import cgi

def build_page(textarea_content,rot):
    header="<h2>Web Caesar</h2>"
    rotation_input = "<label>Rotate by:</label><br><input name='rot' type='number' value="+str(rot)+">"
    textarea="<label>Type a message:</label><br><textarea name='message'>"+textarea_content+"</textarea>"
    submit="<input type='submit'>"
    form="<form method=post>"+rotation_input +"<br>"+ textarea + "<br>"+submit+"</form>"
    content=header+form
    return content



class MainHandler(webapp2.RequestHandler):
    def get(self):

        self.response.write(build_page("",0))

    def post(self):
        message=self.request.get("message")
        rot=self.request.get("rot")

        encrypted_message=caesar.encrypt(message,int(rot))
        escaped_message= cgi.escape(encrypted_message)
        self.response.write(build_page(escaped_message,int(rot)))

app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)
