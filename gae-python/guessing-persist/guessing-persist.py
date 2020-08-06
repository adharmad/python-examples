import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

class GuessInfo(db.Model):
    guess = db.StringProperty()
    msg = db.StringProperty()

class MainPage(webapp.RequestHandler):
    formstring = '''<form method="post" action="/">
        <p>Enter Guess: <input type="text" name="guess" /></p>
        <p><input type="submit"> </p>
        </form>'''

    def get(self):
        self.response.out.write('<p>Good luck!</p>\n')
        self.response.out.write(self.formstring)

    def post(self):
        stguess = self.request.get('guess')
        try:
            guess = int(stguess)
        except:
            guess = -1

        answer = 42

        msg = ''
        if guess == answer:
            msg = 'Congratulations'
        elif guess < 0:
            msg = 'Please provide a number guess'
        elif guess < answer:
            msg = 'Your guess is too low'
        else:
            msg = 'Your guess is too high'

        g = GuessInfo()
        g.guess = str(guess)
        g.msg = msg
        g.put()

        success_msg = ''
        if msg == 'Congratulations':
            past_guess = db.GqlQuery("SELECT * FROM GuessInfo")
            for gg in past_guess:
                success_msg += '<p>' + gg.msg + ' -- ' + gg.guess + '</p>\n'
                #success_msg = 'Hello'

        self.response.out.write('<p>Guess:' + stguess + '</p>\n')
        self.response.out.write('<p>' + msg + '</p>\n')

        if msg == 'Congratulations':
            self.response.out.write('<p>' + success_msg + '</p>\n')
        else:
            self.response.out.write(self.formstring)

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
