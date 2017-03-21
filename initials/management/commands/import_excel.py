import csv
import os

from django.core.management import BaseCommand
from django.core.files import File

from condocument_settings.helpers.enum import PropertyType, Types
from condos.models import Condo, Address, BedroomQuantity, Bedroom, Application

pdf = {
    '1060 Brickell': (
        '1060 Brickell Brickell Condominium Application.pdf', '1060 Brickell Brickell Condominium Application.pdf'),
    'Brickell Bay Club Condo': (
        'Brickell Bay Club Condominium Application Purchase.pdf',
        'Brickell Bay Club Condominium Application Lease.pdf'),
    'Icon Brickell': ('3 Icon Brickell Condominium Application Re-Sale.pdf', '')
}


class Command(BaseCommand):
    fixture_name = 'import_excel'

    def handle(self, *args, **options):
        with open(os.path.join('initials', 'fixture', 'DatabaseCondo.csv'), 'r') as f:
            reader = csv.reader(f)
            trigger = True
            for line in reader:
                if trigger:
                    trigger = False
                    continue
                year = int(line[7]) if line[7] else 0
                sn = int(line[9]) if line[9] else 0
                uu = int(line[10]) if line[10] else 0
                ps = int(line[11]) if line[11] else 0
                fc = line[12].upper() == 'YES'
                pets = line[14].upper() == 'YES'
                vp = line[13].upper() == 'YES'
                pool = line[15].upper() == 'YES'
                address, _ = Address.objects.get_or_create(line_1=line[1], zip_code=line[3], area=line[4])
                condo = Condo.objects.create(name=line[0], address=address, phone=line[5], location=line[6], year=year,
                                             story_number=sn, unit_number=uu, parking_spaces=ps, fitness_center=fc,
                                             pets=pets, valet_parking=vp, pool=pool, market=line[16], county=line[17],
                                             info=line[18])

                ###
                # Sale units
                ###
                studio = Bedroom.objects.get(name='Studio')
                quantity = int(line[21]) if line[21] else 0
                _ = BedroomQuantity.objects.create(bedroom=studio, condo=condo, type=PropertyType.SALE.value,
                                                   quantity=quantity)
                bedroom = Bedroom.objects.get(name='Bedroom', quantity=1)
                quantity = int(line[22]) if line[22] else 0
                _ = BedroomQuantity.objects.create(bedroom=bedroom, condo=condo, type=PropertyType.SALE.value,
                                                   quantity=quantity)

                bedroom = Bedroom.objects.get(name='Bedroom', quantity=2)
                quantity = int(line[23]) if line[23] else 0
                _ = BedroomQuantity.objects.create(bedroom=bedroom, condo=condo, type=PropertyType.SALE.value,
                                                   quantity=quantity)

                bedroom = Bedroom.objects.get(name='Bedroom', quantity=3)
                quantity = int(line[24]) if line[24] else 0
                _ = BedroomQuantity.objects.create(bedroom=bedroom, condo=condo, type=PropertyType.SALE.value,
                                                   quantity=quantity)

                ###
                # Rent Units
                ###

                studio = Bedroom.objects.get(name='Studio')
                quantity = int(line[26]) if line[26] else 0
                _ = BedroomQuantity.objects.create(bedroom=studio, condo=condo, type=PropertyType.RENT.value,
                                                   quantity=quantity)
                bedroom = Bedroom.objects.get(name='Bedroom', quantity=1)
                quantity = int(line[27]) if line[27] else 0
                _ = BedroomQuantity.objects.create(bedroom=bedroom, condo=condo, type=PropertyType.RENT.value,
                                                   quantity=quantity)

                bedroom = Bedroom.objects.get(name='Bedroom', quantity=2)
                quantity = int(line[28]) if line[28] else 0
                _ = BedroomQuantity.objects.create(bedroom=bedroom, condo=condo, type=PropertyType.RENT.value,
                                                   quantity=quantity)

                bedroom = Bedroom.objects.get(name='Bedroom', quantity=3)
                quantity = int(line[29]) if line[29] else 0
                _ = BedroomQuantity.objects.create(bedroom=bedroom, condo=condo, type=PropertyType.RENT.value,
                                                   quantity=quantity)

                ###
                # Application
                ###
                if pdf[condo.name][0] == pdf[condo.name][1]:
                    path = open(os.path.join('initials', 'fixture', 'PDF', pdf[condo.name][0]), 'rb')
                    file = File(path)
                    _ = Application.objects.create(condo=condo, type=Types.BOTH.value, pdf=file)
                    path.close()
                    file.close()
                    continue
                if pdf[condo.name][0]:
                    path = open(os.path.join('initials', 'fixture', 'PDF', pdf[condo.name][0]), 'rb')

                    file = File(path)
                    _ = Application.objects.create(condo=condo, type=Types.PURCHASE.value, pdf=file)
                    path.close()
                    file.close()
                if pdf[condo.name][1]:
                    path = open(os.path.join('initials', 'fixture', 'PDF', pdf[condo.name][1]), 'rb')
                    file = File(path)
                    _ = Application.objects.create(condo=condo, type=Types.RENT.value, pdf=file)
                    file.close()
                    path.close()
                print(str(condo))
