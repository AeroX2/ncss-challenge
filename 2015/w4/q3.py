#!/bin/env python3
from xml.etree.ElementTree import XMLParser
import re


class Test:
    def __init__(self):
        self.stack = []
        self.nodes = []
        self.ATTRIBUTES = {"fill":"#000000",
                  "stroke":"#000000",
                  "stroke-dasharray":"none",
                  "stroke-width":"1",
                  "id":""}

    def start(self, tag, attrib):
        if tag.rfind("}"):
            tag = tag[tag.rfind("}")+1:]
        blub = attrib.copy()
        self.stack.append(blub)
        if tag in ["rect","circle","path"]:
            attributes = {}
            for attribute in self.ATTRIBUTES:
                is_set = False
                if attribute in attrib:
                    attributes[attribute] = attrib[attribute]
                    is_set = True
                else:
                    for item in self.stack[::-1]:
                        if attribute in item:
                            attributes[attribute] = item[attribute]
                            is_set = True
                if not is_set:
                    attributes[attribute] = self.ATTRIBUTES[attribute]
            self.nodes.append(attributes)
                

    def end(self,tag):
        self.stack.pop()
    def data(self, data):
        pass
    def close(self):
        blubfish = sorted(self.nodes, key=lambda x: x["id"])
        for fish in blubfish:
            print('{} fill="{}" stroke="{}" stroke-dasharray="{}" stroke-width="{}"'.format(fish["id"],fish["fill"],fish["stroke"],fish["stroke-dasharray"],fish["stroke-width"]))


parser = XMLParser(target=Test())
xmlstring = open("diagram.svg").read()
parser.feed(xmlstring)
parser.close()
