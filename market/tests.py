from django.test import TestCase
from market.parse import *
from stocktrace.dao.stockdao import *
from market.analysis import *
from market.cix import *
from market.csi import read_index, read_industry, read_index_all, read_industry_all
from market.csi import csi_by_type, read_equity_by_date, read_equity, read_equity_all, read_equity_all2
from market.xueqiu import read_portfolio
# > \Workspace\stocktrace>python manage.py test market.tests.ParseTestCase.test_sh_pe


class ParseTestCase(TestCase):
    code = '600609'
    begin = '2011-05-04'

    def test_xueqiu(self):
        stock = xueqiu(self.code)
        if stock:
            stock.save()

    def test_ah(self):
        ah_history()

    def test_sh_pe(self):
        avg_sh_pe()

    def test_csi(self):
        csi('20170102')

    def test_csi_all(self):
        csi_all('20110503', '20170101')

    def test_csi_industry(self):
        csi_industry('20110503')

    def test_csi_industry_all(self):
        csi_industry_all('20170215', '20171231')

    def test_csi_by_type(self):
        csi_by_type('2018-02-23', 'zy1')

    def test_csi_by_type2(self):
        csi_by_type('2018-02-23', 'zz4')

    def test_read_index(self):
        read_index('2016-01-04')

    def test_read_index_all(self):
        read_index_all('2011-05-04', '2014-12-31')

    def test_read_industry_all(self):
        read_industry_all('2016-01-02', '2016-12-31')

    def test_read_equity_by_date(self):
        read_equity_by_date('2012-10-09', '600436' )

    def test_read_equity(self):
        read_equity('600276', self.begin, '2016-12-31')

    def test_read_equity_all(self):
        read_equity_all(self.begin, '2016-12-31')

    def test_read_equity_all2(self):
        read_equity_all2(self.begin, '2016-12-31')

    def test_hscei(self):
        hs_cei()

    def test_hscei_daily(self):
        hs_cei_daily()

    def test_sz(self):
        market = parse_sz_market()
        if market:
            market.save()

    def test_szzb(self):
        market = parse_szzb_market()
        if market:
            market.save()

    def test_zxb(self):
        market = parse_zxb_market()
        if market:
            market.save()

    def test_cyb(self):
        market = parse_cyb_market()
        if market:
            market.save()

    def test_cyb2(self):
        parse_cyb2()

    def test_gdp(self):
        parse_securitization_rate()

    def test_low_pb(self):
        print(low_pb_ratio())

    def test_high_pb(self):
        print(high_pb_ratio())

    def test_high_price(self):
        high_price_ratio()

    def test_history(self):
        for code in ['600029','601111','600276','600196','002294','601933','601607','002422','002179','600030','601009']:
            history_list = xueqiu_history(code)
            for history in history_list:
                history.save()

    def test_index_history(self):
        for code in ['SH000001', 'SZ399001', 'SZ399005', 'SZ399006']:
            history_list = xueqiu_history(code)
            for history in history_list:
                history.save()

    # def test_history_yahoo(self):
    #     download_history_data(self.code)

    # def test_history_sh(self):
    #     download_history_data('000001.SS')
    #
    # def test_sw_low(self):
    #     df = parse_sw_history('2014-03-12', '2014-03-13')
    #     df_to_collection(df, 'sw')
    #
    # def test_sw_now(self):
    #     import arrow
    #     now = arrow.now()
    #     begin_date = str(now.date())
    #     parse_sw_history(begin_date)

    def test_sw_history(self):
        codes = ['801020', '801030', '801040', '801050', '801080',
                '801110', '801120', '801130', '801140', '801150', '801160', '801170', '801180',
                '801200', '801210', '801230',
                '801710', '801720', '801730', '801740', '801750', '801760', '801770', '801780', '801790',
                '801880', '801890']
        for code in codes:
            df = parse_sw_history2(begin_date='2005-01-01', code=code)
            df_to_collection(df, 'sw')

    def test_sw_history2(self):
        df = parse_sw_history2(begin_date='2015-01-01', code='801150')
        df_to_collection(df, 'sw')

    def test_sw_history3(self):
        df = parse_sw_history2(begin_date='2016-01-01', code='801150')
        print(df)
        records = json.loads(df.T.to_json()).values()
        print(records)

    def test_sw(self):
        sw()

    def test_cix(self):
        cix_data = cix()
        cix_data.save()

    def test_alert(self):
        alert_high_diff()

    def test_read_portfolio(self):
        read_portfolio()

    def test_sh(self):
        sh()
