import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tree.settings')

import django

django.setup()

from tree_menu.models import Menu, MenuItem


def load_data():

    Menu.objects.filter(title="main_menu").delete()

    main_menu = Menu.objects.create(title="main_menu", slug="main_menu")

    forex = MenuItem.objects.create(title="Forex", slug="forex", menu=main_menu)


    major = MenuItem.objects.create(title="Major", slug="major", menu=main_menu, parent=forex)
    minor = MenuItem.objects.create(title="Minor", slug="minor", menu=main_menu, parent=forex)

    major_pairs = ["EU22222D", "U23222PY", "GBdfgdfD", "AUdfgdfSD", "Udfgdf", "dgdgdf", "gggggg", "9808908", "43535", "G90"]

    minor_pairs = ["44444444", "35353535", "U35535", "53535", "U53355", "33453455", "4545556DZAR", "3344455KD", "USD4LN", "U33334"]


    for pair in major_pairs:
        MenuItem.objects.create(title=pair, slug=pair.lower(), parent=major, menu=main_menu)


    for pair in minor_pairs:
        MenuItem.objects.create(title=pair, slug=pair.lower(), parent=minor, menu=main_menu)


    timeframes = [1, 5, 15, 30, 60]
    for pair in major_pairs + minor_pairs:
        pair_item = MenuItem.objects.get(title=pair)

        for timeframe in timeframes:
            timeframe_item = MenuItem.objects.create(title=f"{pair}_{timeframe}", slug=f"{pair.lower()}_{timeframe}",
                                                     parent=pair_item, menu=main_menu)

            MenuItem.objects.create(title=f"{pair}_{timeframe}_ask", slug=f"{pair.lower()}_{timeframe}_ask",
                                    parent=timeframe_item, menu=main_menu)
            MenuItem.objects.create(title=f"{pair}_{timeframe}_bid", slug=f"{pair.lower()}_{timeframe}_bid",
                                    parent=timeframe_item, menu=main_menu)


if __name__ == "__main__":
    print("Loading data...")
    load_data()
    print("Forex menu successfully loaded")



