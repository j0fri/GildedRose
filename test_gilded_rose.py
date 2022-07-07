# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_AgedBrie_increases_quality_before_sellby(self):
        items = [Item("Aged Brie", 10, 0)]
        gilded_rose = GildedRose(items)
        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 5)

    def test_AgedBrie_increases_quality_after_sellby(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 10)

    def test_items_max_quality_50(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        for _ in range(100):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_sulfuras_constant_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 42)]
        gilded_rose = GildedRose(items)
        for _ in range(5):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 42)

    def test_backstages_passes_increases_normally(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(items)
        for _ in range(2):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 12)

    def test_backstages_passes_increases_double(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 10)]
        gilded_rose = GildedRose(items)
        for _ in range(7):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 19)

    def test_backstages_passes_increases_triple(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 7, 10)]
        gilded_rose = GildedRose(items)
        for _ in range(4):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 20)

    def test_backstages_passes_quality_goes_to_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 10)]
        gilded_rose = GildedRose(items)
        for _ in range(4):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_quality_non_negative(self):
        items = [Item("Mongoose", 2, 10)]
        gilded_rose = GildedRose(items)
        for _ in range(500):
            gilded_rose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0)

    def test_double_decay_after_sellby(self):
        items = [Item("Mongoose", 2, 10)]
        gilded_rose = GildedRose(items)
        for _ in range(3):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6)

    def test_conjured_double_decay(self):
        items = [Item("Conjured Mongoose", 5, 10)]
        gilded_rose = GildedRose(items)
        for _ in range(2):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 6)

    def test_conjured_quadruple_decay(self):
        items = [Item("Conjured Mongoose", 2, 20)]
        gilded_rose = GildedRose(items)
        for _ in range(4):
            gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 8)

        
if __name__ == '__main__':
    unittest.main()
