import os

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class U:
    def __init__(self, uid, f, l, a):
        self.uid = uid
        self.first = f
        self.last = l
        self.age = a

class MainPage(webapp.RequestHandler):
    def get(self):
        u1 = U('amol', 'amol', 'dharmadhikari', 35)
        u2 = U('bageshree', 'bageshre', 'dharmadhikari', 31)
        u3 = U('kash', 'kashmira', 'dharmadhikari', 3)
        u4 = U('madhura', 'madhura', 'dalvi', 31)
        testlst = [u1, u2, u3, u4]

        template_values = {
            'users': testlst,
            'a' : 'hello1',
            'xx' : [1, 2, 3]
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

# the wsgi application
application = webapp.WSGIApplication([('/', MainPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

