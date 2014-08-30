#!/usr/bin/env python
from twisted.web import server, resource, http
from bs4 import BeautifulSoup

class RootResource(resource.Resource):
    def __init__(self):
        resource.Resource.__init__(self)
    def getChild(self, path, request):
        if path == 'iliveatmonsterpalace':
            return SetStringResource()
class SetStringResource(resource.Resource):
    def getChild(self, path, request):
        return self
    def render_GET(self, request):
        args = request.args
        if 'answer' in args:
            answer = args['answer'][0]
            soup = BeautifulSoup(open('/usr/share/nginx/www/index.html').read())
            tag = soup.find("h1")
            tag.string.replace_with(answer)
            fl = open('/usr/share/nginx/www/index.html', 'w')
            fl.write(soup.prettify())
        request.setResponseCode(http.OK)
        return "success!"
if __name__ == "__main__":
    from twisted.internet import reactor
    reactor.listenTCP(8082, server.Site(RootResource()))
    reactor.run()
