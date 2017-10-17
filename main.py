import tornado.escape
import tornado.ioloop
import tornado.web

from webserver.analyse_pool_stocks import FindPoolStocks
from webserver.calc_range_trend import CalcRangeTrend
from webserver.loginManager import loginManager
from webserver.save_upload_excel import SaveSuggestExcel
from webserver.stock_of_consultor_history import FindStockSuggestHistory
from webserver.suggest_history import FindHistorySuggest
from webserver.suggestwithtrends import HandleSuggestTrends


def make_app():
    return tornado.web.Application([
        (r"/upload/recommond", SaveSuggestExcel),
        (r"/history/suggest", FindHistorySuggest),
        (r"/history/suggest/detail", FindStockSuggestHistory),
        (r"/analyse/rangetrend", CalcRangeTrend),
        (r"/history/suggestwithtrends", HandleSuggestTrends),
        (r"/analyse/poolstock", FindPoolStocks),
        (r"/login", loginManager),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()