from portui.controllers import BaseHandler
import tornado.web


class params:
    route='/entry/([0-9]+)'
    pass

class Handler(BaseHandler):
    @tornado.web.removeslash
    def get(self, id=None):
        self.render('entry.html')
