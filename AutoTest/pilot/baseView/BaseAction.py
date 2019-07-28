#!/usr/bin/python3
# encoding:utf-8

class BaseAction(object):
    def __init__(self):

    def find_element(self, *loc):
        pass

    def find_elements(self, *loc):
        pass

    def get_window_size(self):
        pass

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        pass
