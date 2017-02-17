
import webapp2

form = """
<form action="/testHandler">
    <input name="q">
    <input type="submit">
</from>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(form)

class testHandler(webapp2.RequestHandler):
    def get(self):
        q=self.request.get('q')
        self.response.write(q)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testHandler' , testHandler)
], debug=True)
