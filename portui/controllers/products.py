from portui.controllers import BaseHandler
import tornado.web
from random import randrange



class params:
    route=['/products/?([0-9]+)',
           '/products/*']
    pass

class Handler(BaseHandler):
    @tornado.web.removeslash
    def get(self, id=None):
        if id is None:
            self.render('products.html')
        else:
            names = {'Documentation': 'rgba(235,237,201,0.5)',
                    'Architectural Operability': 'rgba(132,111,153,0.5)',
                    'Recoverability': 'rgba(117,293,33,0.5)',
                    'Llama! - Logging, Alerting, Monitoring': 'rgba(29,84,152,0.5)',
                    'Automation': 'rgba(73,192,247,0.5)',
                    'Standards': 'rgba(86,278,215,0.5)'}
            colors = []
            for name in names:
                colors.append(names[name])
            scores = ['Level 1 - Ad Hoc',
                    'Level 2 - Standardizing',
                    'Level 3 - Industry Standard',
                    'Level 5 - Industry Leader',
                    'Level 8 - World Class']

            datasets = {'0': [randrange(1,9) for x in range(9)],
                        '1': [randrange(1,9) for x in range(9)],
                        '2': [randrange(1,9) for x in range(9)],
                        '3': [randrange(1,9) for x in range(9)],
                        '4': [randrange(1,9) for x in range(9)],
                        '5': [randrange(1,9) for x in range(9)]}

            self.render('product.html', id=id, names=names, scores=scores, randrange=randrange, datasets=datasets, colors=colors)
