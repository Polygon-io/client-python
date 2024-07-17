from base import BaseTest

from polygon.rest.models import Agg


class ModelclassTest(BaseTest):
    def test_extra_field(self):
        with self.assertRaises(TypeError):
            b = Agg(
                open=1.5032,
                high=1.5064,
                low=1.4489,
                close=1.4604,
                volume=642646396.0,
                vwap=1.469,
                timestamp=1112331600000,
                transactions=82132,
                extra_field=22,
            )

    def test_init_order(self):
        a = Agg(
            open=1.5032,
            high=1.5064,
            low=1.4489,
            close=1.4604,
            volume=642646396.0,
            vwap=1.469,
            timestamp=1112331600000,
            transactions=82132,
        )
        b = Agg(
            1.5032,
            1.5064,
            1.4489,
            1.4604,
            642646396.0,
            1.469,
            1112331600000,
            82132,
        )
        self.assertEqual(a, b)
