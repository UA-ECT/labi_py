import cherrypy

#pagina HTML
class HTMLDocument (object):

    #index da pagina html
    
    @cherrypy.expose
    def index (self) :
        return open("Documento.html")

    #formulario
    
    @cherrypy.expose
    def form(self):
        cherrypy.response.headers["Content-Type"] = "text/html"
        return open("formulario.html", "r").read()

class Node(object):
    @cherrypy.expose
    def index(self):
        return "Eu sou o índice do Node (Node.index)"
    
    @cherrypy.expose
    def page(self):
        return "You sou um método do Node (Node.page)"

class Root(object):
    def __init__(self):
        self.node = Node()
        self.HTML = HTMLDocument()

    @cherrypy.expose
    def index(self):
        return "Eu sou o índice do Root (Root.index)"
    
    @cherrypy.expose
    def page(self):
        return "Eu sou um método do Root (Root.page)"

if __name__ == "__main__":
   cherrypy.quickstart(Root()) 
