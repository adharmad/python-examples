from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            resout = 'Hello: ' + user.nickname() + '\nEmail: ' + user.email() 
            self.response.out.write(resout)
            if users.is_current_user_admin():
                print "<a href=\"/admin/\">Go to admin area</a>"
        else:
            self.redirect(users.create_login_url(self.request.uri))

class LoginLogoutHandler(webapp.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
                        (user.nickname(), users.create_logout_url("/")))
        else:
            greeting = ("<a href=\"%s\">Sign in or register</a>." %
                        users.create_login_url("/"))

        self.response.out.write("<html><body>%s</body></html>" % greeting)


application = webapp.WSGIApplication([('/', MainPage), ('/test1', LoginLogoutHandler)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
