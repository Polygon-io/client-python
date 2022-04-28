from polygon import RESTClient
import unittest
import httpretty  # type: ignore

mocks = [
    (
        "/v2/aggs/ticker/AAPL/range/1/day/2005-04-01/2005-04-04",
        '{"ticker":"AAPL","queryCount":2,"resultsCount":2,"adjusted":true,"results":[{"v":6.42646396e+08,"vw":1.469,"o":1.5032,"c":1.4604,"h":1.5064,"l":1.4489,"t":1112331600000,"n":82132},{"v":5.78172308e+08,"vw":1.4589,"o":1.4639,"c":1.4675,"h":1.4754,"l":1.4343,"t":1112587200000,"n":65543}],"status":"OK","request_id":"12afda77aab3b1936c5fb6ef4241ae42","count":2}',
    ),
    (
        "/v2/aggs/grouped/locale/us/market/stocks/2005-04-04",
        '{"queryCount":1,"resultsCount":1,"adjusted": true,"results": [{"T":"GIK","v":895345,"vw":9.9979,"o":9.99,"c":10.02,"h":10.02,"l":9.9,"t":1602705600000,"n":96}],"status":"OK","request_id":"eae3ded2d6d43f978125b7a8a609fad9","count":1}',
    ),
    (
        "/v1/open-close/AAPL/2005-04-01",
        '{"status": "OK","from": "2021-04-01","symbol": "AAPL","open": 123.66,"high": 124.18,"low": 122.49,"close": 123,"volume": 75089134,"afterHours": 123,"preMarket": 123.45}',
    ),
    (
        "/v2/aggs/ticker/AAPL/prev",
        '{"ticker":"AAPL","queryCount":1,"resultsCount":1,"adjusted":true,"results":[{"T":"AAPL","v":9.5595226e+07,"vw":158.6074,"o":162.25,"c":156.8,"h":162.34,"l":156.72,"t":1651003200000,"n":899965}],"status":"OK","request_id":"5e5378d5ecaf3df794bb52e45d015d2e","count":1}',
    ),
    (
        "/v3/reference/tickers",
        '{"results":[{"ticker":"A","name":"Agilent Technologies Inc.","market":"stocks","locale":"us","primary_exchange":"XNYS","type":"CS","active":true,"currency_name":"usd","cik":"0001090872","composite_figi":"BBG000C2V3D6","share_class_figi":"BBG001SCTQY4","last_updated_utc":"2022-04-27T00:00:00Z"},{"ticker":"AA","name":"Alcoa Corporation","market":"stocks","locale":"us","primary_exchange":"XNYS","type":"CS","active":true,"currency_name":"usd","cik":"0001675149","composite_figi":"BBG00B3T3HD3","share_class_figi":"BBG00B3T3HF1","last_updated_utc":"2022-04-27T00:00:00Z"}],"status":"OK","request_id":"37089bb3b4ef99a796cdc82ff971e447","count":2,"next_url":"https://api.polygon.io/v3/reference/tickers?cursor=YWN0aXZlPXRydWUmZGF0ZT0yMDIyLTA0LTI3JmxpbWl0PTImb3JkZXI9YXNjJnBhZ2VfbWFya2VyPUFBJTdDZjEyMmJjYmY4YWQwNzRmZmJlMTZmNjkxOWQ0ZDc3NjZlMzA3MWNmNmU1Nzg3OGE0OGU1NjQ1YzQyM2U3NzJhOSZzb3J0PXRpY2tlcg"}',
    ),
    (
        "/v3/reference/tickers?cursor=YWN0aXZlPXRydWUmZGF0ZT0yMDIyLTA0LTI3JmxpbWl0PTImb3JkZXI9YXNjJnBhZ2VfbWFya2VyPUFBJTdDZjEyMmJjYmY4YWQwNzRmZmJlMTZmNjkxOWQ0ZDc3NjZlMzA3MWNmNmU1Nzg3OGE0OGU1NjQ1YzQyM2U3NzJhOSZzb3J0PXRpY2tlcg",
        '{"results":[{"ticker":"AAA","name":"AAF First Priority CLO Bond ETF","market":"stocks","locale":"us","primary_exchange":"ARCX","type":"ETF","active":true,"currency_name":"usd","composite_figi":"BBG00X5FSP48","share_class_figi":"BBG00X5FSPZ4","last_updated_utc":"2022-04-27T00:00:00Z"},{"ticker":"AAAU","name":"Goldman Sachs Physical Gold ETF Shares","market":"stocks","locale":"us","primary_exchange":"BATS","type":"ETF","active":true,"currency_name":"usd","cik":"0001708646","composite_figi":"BBG00LPXX872","share_class_figi":"BBG00LPXX8Z1","last_updated_utc":"2022-04-27T00:00:00Z"}],"status":"OK","request_id":"40d60d83fa0628503b4d13387b7bde2a","count":2}',
    ),
    (
        "/v3/reference/tickers/AAPL",
        '{"ticker":"AAPL","name":"Apple Inc.","market":"stocks","locale":"us","primary_exchange":"XNAS","type":"CS","active":true,"currency_name":"usd","cik":"0000320193","composite_figi":"BBG000B9XRY4","share_class_figi":"BBG001S5N8V8","market_cap":2.6714924917e+12,"phone_number":"(408) 996-1010","address":{"address1":"ONE APPLE PARK WAY","city":"CUPERTINO","state":"CA","postal_code":"95014"},"description":"Apple designs a wide variety of consumer electronic devices, including smartphones (iPhone), tablets (iPad), PCs (Mac), smartwatches (Apple Watch), AirPods, and TV boxes (Apple TV), among others. The iPhone makes up the majority of Apples total revenue. In addition, Apple offers its customers a variety of services such as Apple Music, iCloud, Apple Care, Apple TV+, Apple Arcade, Apple Card, and Apple Pay, among others. Apples products run internally developed software and semiconductors, and the firm is well known for its integration of hardware, software and services. Apples products are distributed online as well as through company-owned stores and third-party retailers. The company generates roughly 40 of its revenue from the Americas, with the remainder earned internationally.","sic_code":"3571","sic_description":"ELECTRONIC COMPUTERS","ticker_root":"AAPL","homepage_url":"https://www.apple.com","total_employees":154000,"list_date":"1980-12-12","branding":{"logo_url":"https://api.polygon.io/v1/reference/company-branding/d3d3LmFwcGxlLmNvbQ/images/2022-02-01_logo.svg","icon_url":"https://api.polygon.io/v1/reference/company-branding/d3d3LmFwcGxlLmNvbQ/images/2022-02-01_icon.png"},"share_class_shares_outstanding":16319440000,"weighted_shares_outstanding":16319441000}',
    ),
    (
        "/v2/reference/news",
        '{"results":[{"id":"JeJEhAVoKaqJ2zF9nzQYMg07UlEeWlis6Dsop33TPQY","publisher":{"name":"MarketWatch","homepage_url":"https://www.marketwatch.com/","logo_url":"https://s3.polygon.io/public/assets/news/logos/marketwatch.svg","favicon_url":"https://s3.polygon.io/public/assets/news/favicons/marketwatch.ico"},"title":"Theres a big hole in the Feds theory of inflation—incomes are falling at a record 10.9 rate","author":"MarketWatch","published_utc":"2022-04-28T17:08:00Z","article_url":"https://www.marketwatch.com/story/theres-a-big-hole-in-the-feds-theory-of-inflationincomes-are-falling-at-a-record-10-9-rate-11651165705","tickers":["MSFT","TSN","NFLX","AMZN"],"amp_url":"https://www.marketwatch.com/amp/story/theres-a-big-hole-in-the-feds-theory-of-inflationincomes-are-falling-at-a-record-10-9-rate-11651165705","image_url":"https://images.mktw.net/im-533637/social","description":"If inflation is all due to an overly generous federal government giving its people too much money, then our inflation problem is about to go away."}],"status":"OK","request_id":"f5248459196e12f27520afd41cee5126","count":10}',
    ),
    (
        "/v3/reference/tickers/types",
        '{"results":[{"code":"CS","description":"Common Stock","asset_class":"stocks","locale":"us"},{"code":"PFD","description":"Preferred Stock","asset_class":"stocks","locale":"us"},{"code":"WARRANT","description":"Warrant","asset_class":"stocks","locale":"us"},{"code":"RIGHT","description":"Rights","asset_class":"stocks","locale":"us"},{"code":"BOND","description":"Corporate Bond","asset_class":"stocks","locale":"us"},{"code":"ETF","description":"Exchange Traded Fund","asset_class":"stocks","locale":"us"},{"code":"ETN","description":"Exchange Traded Note","asset_class":"stocks","locale":"us"},{"code":"SP","description":"Structured Product","asset_class":"stocks","locale":"us"},{"code":"ADRC","description":"American Depository Receipt Common","asset_class":"stocks","locale":"us"},{"code":"ADRW","description":"American Depository Receipt Warrants","asset_class":"stocks","locale":"us"},{"code":"ADRR","description":"American Depository Receipt Rights","asset_class":"stocks","locale":"us"},{"code":"FUND","description":"Fund","asset_class":"stocks","locale":"us"},{"code":"BASKET","description":"Basket","asset_class":"stocks","locale":"us"},{"code":"UNIT","description":"Unit","asset_class":"stocks","locale":"us"},{"code":"LT","description":"Liquidating Trust","asset_class":"stocks","locale":"us"}],"status":"OK","request_id":"efbfc7c2304bba6c2f19a2567f568134","count":15}',
    ),
]


class BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = None
        cls.c = RESTClient("")
        httpretty.enable(verbose=True, allow_net_connect=False)
        for m in mocks:
            httpretty.register_uri(httpretty.GET, cls.c.BASE + m[0], m[1])
