from portui.controllers import BaseHandler
import tornado.web


class params:
    route='/entry/new'
    pass

class Handler(BaseHandler):
    @tornado.web.removeslash
    def get(self):
        self.render('new_entry.html')
