from portui.controllers import BaseHandler
import tornado.web


class params:
    route='/products/*'
    pass

class Handler(BaseHandler):
    @tornado.web.removeslash
    def get(self):
        self.render('products.html')
