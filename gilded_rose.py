# -*- coding: utf-8 -*-



class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name.startswith("Conjured"):     # Handles the cases where items can
                item_type = "Conjured"               # start with a name, rather than have a name
            elif item.name.startswith("Sulfuras"):
                item_type = "Sulfuras"
            else:
                item_type = item.name

            change = -1 if item.sell_in > 0 else -2
            match item_type:
                case "Aged Brie":
                    change *= -1
                case "Sulfuras":
                    change = 0
                case "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in > 10:
                        change *= -1
                    elif 5 < item.sell_in:    # 5 < sell_in <= 10
                        change *= -2
                        print("Double")
                    elif item.sell_in > 0:
                        change *= -3
                    else:
                        change = 0        # Quality goes to 0 once concert has passed
                        item.quality = 0

                case "Conjured":
                    change *= 2

            if item_type != "Sulfuras":
                item.sell_in -= 1

            item.quality = min(50, max(0, item.quality + change))


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
