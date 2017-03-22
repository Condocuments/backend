import csv
import datetime
import os
from dateutil.parser import parse
from django.core.management import BaseCommand

from condocument_settings.helpers.enum import PropertyType
from condos.models import Condo, Unit


def fix_price(price):
    tmp = price.replace('$', '').replace(',', '').replace('.', '').replace('-', '').strip()
    return int(tmp) if tmp else 0


def fix_date(date):
    _date = date.split()[0]
    return parse(_date)


class Command(BaseCommand):
    fixture_name = 'import_excel_units'

    def handle(self, *args, **options):
        with open(os.path.join('initials', 'fixture', 'DatabaseUnit.csv'), 'r') as f:
            reader = csv.reader(f)
            trigger = True
            for line in reader:
                if trigger:
                    trigger = False
                    continue
                price = fix_price(line[7])
                beds = int(line[8]) if line[8] else 0
                fbaths = int(line[9]) if line[9] else 0
                hbaths = int(line[10]) if line[10] else 0
                live_area = fix_price(line[11])
                association_fee = fix_price(line[12])
                year = int(line[14]) if line[14] else 0
                garage_spaces = int(line[15]) if line[15] else 0
                pool = line[16].upper() == 'YES'
                wf = line[17].upper() == 'YES'
                cp = fix_price(line[18])
                ed = fix_date(line[19])
                dm = int(line[20]) if line[20] else 0
                rp = line[22] if line[22] else '---'
                pt = PropertyType.SALE.value if line[21].lower() == 'for sale' else PropertyType.RENT.value
                furnished = line[23].lower() == 'furnished'

                condo = Condo.objects.get(name=line[6])
                unit = Unit.objects.create(mls_number=line[1], status=line[2], area=line[3], number=line[5],
                                           condo=condo, list_price=price, beds=beds, f_baths=fbaths, h_baths=hbaths,
                                           live_area=live_area, association_fee=association_fee, year=year,
                                           garage_spot=garage_spaces, pool=pool, waterfront=wf, current_price=cp,
                                           entry_date=ed, days_market=dm, property_type=pt, rent_period=rp,
                                           furnished=furnished)

                print(str(unit))
