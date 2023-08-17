import random
import string
import uuid
import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def dash(self):
        cherrypy.response.cookie['sessionid'] = str(cherrypy.session.id)
        raise cherrypy.HTTPRedirect("http://127.0.0.1:8050/")

    @cherrypy.expose
    def generate(self,length = 16):
        cherrypy.session['s_id'] = uuid.uuid4();
        return ''.join(random.sample(string.hexdigits, int(length))) + "___hello___" + str(cherrypy.session.get('s_id')) + "___hello___" + str(cherrypy.session.id)


if __name__ == '__main__':
    # cherrypy.expose()
    cherrypy.quickstart(StringGenerator(),  '/', "app.conf")
    print("hello")
    # cherrypy.lib
