# -*- coding: utf-8 -*-
"""
Created on Mon May  9 13:00:40 2016

@author: Arti
"""
from shapely.geometry import Polygon, Point
from pyproj import Proj, transform
import json

promien = 250.0 # w jakim promieniu od stacji (w metrach)

lokalizacje = []
_0___2 = []
_3___6 = []
_7___12 = []
_13___15 = []
_16___18 = []
_19___24 = []
_25___34 = []
_35___44 = []
_45___59k___64m = []
_60k___65m___79 = []
_80__ = []
ilosc_osob_zameldowanych = []
coordinates = []
szer_geograficzna = []
dl_geograficzna = []
INPUT_PATH = 'stacje_wrm_2016.geojson'
plik = open(INPUT_PATH, encoding="utf8")
json_data = plik.read()
data = json.loads(json_data)
for feature in data['features']:
    geo = feature['geometry']
    prop = feature['properties']
    lokalizacje.append(prop.pop('lokalizacja'))
    szer_geograficzna.append(prop.pop('szer_geograficzna'))
    dl_geograficzna.append(prop.pop('dl_geograficzna'))
plik.close()

INPUT_PATH = 'demografia_wroclawia_2014_wg_rejonow_brec_2011.geojson'
plik = open(INPUT_PATH, encoding="utf8")
json_data = plik.read()
data = json.loads(json_data)
for feature in data['features']:
    geo = feature['geometry']
    prop = feature['properties']
    _0___2.append(prop.pop('_0___2'))
    _3___6.append(prop.pop('_3___6'))
    _7___12.append(prop.pop('_7___12'))
    _13___15.append(prop.pop('_13___15'))
    _16___18.append(prop.pop('_16___18'))
    _19___24.append(prop.pop('_19___24'))
    _25___34.append(prop.pop('_25___34'))
    _35___44.append(prop.pop('_35___44'))
    _45___59k___64m.append(prop.pop('_45___59k___64m'))
    _60k___65m___79.append(prop.pop('_60k___65m___79'))
    _80__.append(prop.pop('_80__'))
    ilosc_osob_zameldowanych.append(prop.pop('ilosc_osob_zameldowanych'))
    coordinates.append(geo.pop('coordinates'))

wyjscie = [[] for i in range(len(dl_geograficzna) + 1)]
wyjscie[0].append('lokalizacja')
wyjscie[0].append('ilosc_osob_zameldowanych')
wyjscie[0].append('_0___2')
wyjscie[0].append('_3___6')
wyjscie[0].append('_7___12')
wyjscie[0].append('_13___15')
wyjscie[0].append('_16___18')
wyjscie[0].append('_19___24')
wyjscie[0].append('_25___34')
wyjscie[0].append('_35___44')
wyjscie[0].append('_45___59k___64m')
wyjscie[0].append('_60k___65m___79')
wyjscie[0].append('_80__')

proj2 = Proj(init = 'epsg:2180')
proj1 = Proj(init = 'epsg:4326')

for i in range(len(dl_geograficzna)):
    x1, y1 = dl_geograficzna[i], szer_geograficzna[i]
    x2, y2 = transform(proj1, proj2, x1, y1)
    p = Point(x2, y2)
    circle = p.buffer(promien)
    x3, y3 = circle.exterior.coords.xy
    x, y = transform(proj2, proj1, x3, y3)
    poly1 = Polygon([(x[j],y[j]) for j in range(len(x))])
    s_0___2 = 0
    s_3___6 = 0
    s_7___12 = 0
    s_13___15 = 0
    s_16___18 = 0
    s_19___24 = 0
    s_25___34 = 0
    s_35___44 = 0
    s_45___59k___64m = 0
    s_60k___65m___79 = 0
    s_80__ = 0
    silosc_osob_zameldowanych = 0
    for j in range(len(coordinates)):
        poly2 = Polygon(coordinates[j][0])
        intersection = poly1.intersection(poly2)
        d = intersection.area
        if d != 0:
            s_0___2 += _0___2[j]
            s_3___6 += _3___6[j]
            s_7___12 += _7___12[j]
            s_13___15 += _13___15[j]
            s_16___18 += _16___18[j]
            s_19___24 += _19___24[j]
            s_25___34 += _25___34[j]
            s_35___44 += _35___44[j]
            s_45___59k___64m += _45___59k___64m[j]
            s_60k___65m___79 += _60k___65m___79[j]
            s_80__ += _80__[j]
            silosc_osob_zameldowanych += ilosc_osob_zameldowanych[j]
    wyjscie[i + 1].append(lokalizacje[i])
    wyjscie[i + 1].append(silosc_osob_zameldowanych)
    wyjscie[i + 1].append(s_0___2)
    wyjscie[i + 1].append(s_3___6)
    wyjscie[i + 1].append(s_7___12)
    wyjscie[i + 1].append(s_13___15)
    wyjscie[i + 1].append(s_16___18)
    wyjscie[i + 1].append(s_19___24)
    wyjscie[i + 1].append(s_25___34)
    wyjscie[i + 1].append(s_35___44)
    wyjscie[i + 1].append(s_45___59k___64m)
    wyjscie[i + 1].append(s_60k___65m___79)
    wyjscie[i + 1].append(s_80__)

import csv
with open('nowy.csv', 'w', newline='') as csvfile:
    nastepny = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(dl_geograficzna) + 1):
        nastepny.writerow(wyjscie[i])
