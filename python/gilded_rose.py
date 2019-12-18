# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                item.quality += 1
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            elif item.name.startswith("Backstage passes"):
                item.sell_in -= 1
                if item.sell_in <= 10 and item.sell_in > 5:
                    item.quality += 2
                elif item.sell_in <= 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality += 3
                else:
                    item.quality += 1
            else:
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality -= 2
                else:
                    item.quality -= 1

            if item.quality < 0:
                item.quality = 0
            if item.quality > 50:
                item.quality = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
