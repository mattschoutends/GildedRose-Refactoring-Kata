# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo_quality_never_below_zero(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        self.assertEqual(0, items[0].quality)

    def test_foo_quality_decreases_by_one(self):
        items = [Item("foo", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_foo_quality_decreases_twice_as_fast_after_sell_date(self):
        items = [Item("foo", -1, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_foo_sellin_decreases_by_one(self):
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_increases_in_quality_up_to_50(self):
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_does_not_decrease_in_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].quality)

    def test_sulfuras_sellin_does_not_decreases(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)

    def test_backstage_passes_quality_increases_by_two_ten_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)

    def test_backstage_passes_quality_increases_by_three_five_days_or_less(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(6, items[0].quality)

    def test_backstage_passes_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
