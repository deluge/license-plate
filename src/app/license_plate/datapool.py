import csv

from django.contrib.staticfiles.finders import find


LICENSE_PLATE_DICT = {}
with open(find("german_license_plates.csv"), newline="") as csvfile:
    for row in csv.reader(csvfile, delimiter=";"):
        LICENSE_PLATE_DICT[row[0]] = row[1]


class LicensePlatePool:
    def city_plate_exists(self, city_shortcut):
        return city_shortcut in LICENSE_PLATE_DICT.keys()
