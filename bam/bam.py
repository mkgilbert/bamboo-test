#!/usr/bin/evn python

class Bam:
    def __init__(self, height):
        self.height = height

    def grow(self, ht):
        self.height += ht
        return self.height

    def __str__(self):
        return "height is %s" % self.height
