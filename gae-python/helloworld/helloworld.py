from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')

class AnotherPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, this is a test!!!')

# invoke using:
# http://localhost:8080/add?first=1&second=2
class AddTwoNumbersPage(webapp.RequestHandler):
    def get(self):
        try:
            first = int(self.request.get('first'))
            second = int(self.request.get('second'))
        
            self.response.out.write("<html><body><p>%d + %d = %d</p></body></html>" % (first, second, first + second))
        except (TypeError, ValueError):
            self.response.out.write("<html><body><p>Invalid inputs</p></body></html>")

class SumOfNumbersPage(webapp.RequestHandler):
    def get(self):
        resout = """
            <html>
                <title>Sum of two numbers</title>
                <body>
                    <form action="/sum" method="post">
                        First number: 
                        <input type="text" name="firstnum">
                        <br>
                        Second number: 
                        <input type="text" name="secondnum">
                        <br>
                        <input type="submit" value="AddEm">
                    </form>
                    <br>
                    Sum of numbers: 
                </body>
            </html>
        """
        self.response.out.write(resout)

    def post(self):
        try:
            first = int(self.request.get('firstnum'))
            second = int(self.request.get('secondnum'))

            resout = """
                <html>
                    <title>Sum of two numbers</title>
                    <body>
                        <form action="/sum" method="post">
                            First number: 
                            <input type="text" name="firstnum">
                            <br>
                            Second number: 
                            <input type="text" name="secondnum">
                            <br>
                            <input type="submit" value="AddEm">
                        </form>
                        <br>
                        Sum of numbers: %d
                    </body>
                </html>
            """
        
            self.response.out.write(resout % (first + second))
        except (TypeError, ValueError):
            self.response.out.write("<html><body><p>Invalid inputs</p></body></html>")


# the wsgi application
application = webapp.WSGIApplication(
    [('/', MainPage), 
    ('/test', AnotherPage), 
    ('/add', AddTwoNumbersPage), 
    ('/sum', SumOfNumbersPage)], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
