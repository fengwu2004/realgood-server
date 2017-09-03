import tornado.escape
import tornado.ioloop
import tornado.web

from webserver.calc_range_trend import CalcRangeTrend
from webserver.save_recommond import SaveRecommond
from webserver.loginManager import loginManager

def make_app():
    return tornado.web.Application([
        (r"/save/saverecommondinfo", SaveRecommond),
        (r"/analyse/rangetrend", CalcRangeTrend),
        (r"/login", loginManager),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()