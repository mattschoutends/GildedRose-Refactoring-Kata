# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        QUALITY_RATE = 1

        for item in self.items:
            if item.name == "Aged Brie":
                item.quality += QUALITY_RATE
            elif item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
                pass
            elif item.name.startswith("Conjured"):
                item.quality -= 2 * QUALITY_RATE
            elif item.name.startswith("Backstage passes"):
                item.sell_in -= 1
                if item.sell_in <= 0:
                    item.quality = 0
                elif item.sell_in <= 10 and item.sell_in > 5:
                    item.quality += 2
                elif item.sell_in <= 5:
                    item.quality += 3
                else:
                    item.quality += QUALITY_RATE
            else:
                item.sell_in -= 1
                if item.sell_in < 0:
                    item.quality -= 2 * QUALITY_RATE
                else:
                    item.quality -= 1 * QUALITY_RATE

            if item.quality < 0:
                item.quality = 0
            if item.quality > 50 and item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = 50
            
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
