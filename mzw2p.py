# -*- coding: utf-8 -*-

from gluon.html import URL
from gluon.sqlhtml import SQLFORM


def Q(txt, cnt=None):
    if cnt is None or '%d' not in txt:
        return txt
    return txt % cnt

def form(tbl, **kwargs):
    next = kwargs.pop('next', URL('default', 'index'))
    form = SQLFORM(tbl, **kwargs)
    if form.process().accepted:
        redirect(next)
    return form
