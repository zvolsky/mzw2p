# -*- coding: utf-8 -*-

def Q(txt, cnt=None):
    if cnt is None or '%d' not in txt:
        return txt
    return txt % cnt
