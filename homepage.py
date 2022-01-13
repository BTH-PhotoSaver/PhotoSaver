#!/usr/bin/python3

from constants import HOMEPAGE_TITLE, HOMEPAGE_TPL
from bottle import template


class Homepage:
    def __init__(self, image_store):
        self.image_items = image_store.fetch_all()

    def render(self):
        return template(HOMEPAGE_TPL, name=HOMEPAGE_TITLE, items=self.image_items)
