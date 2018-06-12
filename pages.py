from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class CRT(Page):
    form_model = 'player'
    form_fields = ['crt_1',
                   'crt_2',
                   'crt_3',
                   'crt_4',
                   ]


page_sequence = [
    CRT
]
