import tornado.escape
import tornado.ioloop
import tornado.web
from saveRecommond import SaveRecommond
from loginManager import loginManager


def make_app():
    return tornado.web.Application([
        (r"/save/saverecommondinfo", SaveRecommond),
        (r"/login", loginManager),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()