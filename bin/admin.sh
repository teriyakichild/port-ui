#!/bin/bash

if [ "$1" == "controller" ] ; then
    if [ "$2" == "add" ] ; then
        if [ "$3" == "" ] ; then
            echo 'missing controller name'
            exit 1
        else
            cp "portui/templates/example.html" "portui/templates/${3}.html"
            echo "from portui.controllers import BaseHandler
import tornado.web


class params:
    route='/${3}/([0-9]+)'
    pass

class Handler(BaseHandler):
    @tornado.web.removeslash
    def get(self, id=None):
        self.render('${3}.html', id=id)" > "portui/controllers/${3}.py"
        fi
    else
        echo "missing method"
        exit 1
    fi
else
    echo "missing type"
    exit 1  
fi
