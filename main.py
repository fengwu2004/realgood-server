import tornado.escape
import tornado.ioloop
import tornado.web

from webserver.calc_range_trend import CalcRangeTrend
from webserver.save_recommond import SaveRecommond
from webserver.loginManager import loginManager
from webserver.save_upload_excel import SaveRecommondExcel
from webserver.stock_of_consultor_history import FindStockSuggestHistory
from webserver.suggest_history import FindHistorySuggest


def make_app():
    return tornado.web.Application([
        (r"/save/saverecommondinfo", SaveRecommond),
        (r"/upload/recommond", SaveRecommondExcel),
        (r"/history/suggest", FindHistorySuggest),
        (r"/history/suggest/stockhistory", FindStockSuggestHistory),
        (r"/analyse/rangetrend", CalcRangeTrend),
        (r"/login", loginManager),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()