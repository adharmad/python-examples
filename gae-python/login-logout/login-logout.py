import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class LoginHandler(webapp.RequestHandler):
    def get(self):
        doRender(self, 'loginscreen.htm')

    def post(self):
        self.session = Session()
        acct = self.request.get('account')
        pw = self.request.get('password')
        logging.info('Checking account=' + acct + ' password=' + pw)
        self.session.delete_item('username')

        if pw == '' or acct == '':
            doRender(self, 'loginscreen.htm',
                {'error' : 'Please specify valid username and
                    password'})
        elif pw == 'secret':
            self.session['username'] = acct
            doRender(self, 'index.htm', {})
        else:
            doRender(self, 'loginscreen.htm', 
                {'error' : 'Incorrect password'}

application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/sign', Guestbook)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
