#!/bin/sh

all=/home/mengf1/ariel_data/misc_resources/geonames_20160929/allCountries.txt
alt=/home/mengf1/ariel_data/misc_resources/geonames_20160929/alternateNames.txt

python extractUgGeoNames.py $all $alt locations.tsv
