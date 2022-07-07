# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):

        class ItemType:
            general = 0
            brie = 1
            sulfuras = 2
            backstage_pass = 3
            conjured = 4

        for item in self.items:
            if item.name == "Aged Brie":
                item_type = ItemType.brie
            elif item.name.startswith("Conjured"):     # Handles the cases where items can
                item_type = ItemType.conjured          # start with a name, rather than have a name
            elif item.name.startswith("Sulfuras"):
                item_type = ItemType.sulfuras
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item_type = ItemType.backstage_pass
            else:
                item_type = ItemType.general

            change = -1 if item.sell_in > 0 else -2
            match item_type:
                case ItemType.brie:
                    change *= -1
                case ItemType.sulfuras:
                    change = 0
                case ItemType.backstage_pass:
                    if item.sell_in > 10:
                        change *= -1
                    elif 5 < item.sell_in:    # 5 < sell_in <= 10
                        change *= -2
                    elif item.sell_in > 0:
                        change *= -3
                    else:
                        change = 0        # Quality goes to 0 once concert has passed
                        item.quality = 0

                case ItemType.conjured:
                    change *= 2

            if item_type != ItemType.sulfuras:
                item.sell_in -= 1

            item.quality = min(50, max(0, item.quality + change))


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
