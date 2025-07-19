import json
import urllib.request
import string
import sys
import re
req = urllib.request.Request(url=f'https://marketplace.worten.pt/api/offers/27797160')
#key = 'ff60c24a-734b-4fd0-8ed5-ad33afcdacc7'
#req.add_header("Authorization", key)
with urllib.request.urlopen(req) as resp:
    json_offer = json.loads(resp.read().decode("utf-8"))
    description = json_offer['offer_additional_fields']
    contpt = contes = 0

    for x in description:
        if x['code'] == 'description-pt':
            description_pt = (x['value'])
            contpt += 1
        if x['code'] == 'description-es':
            description_es = (x['value'])
            contes += 1
    if contes == 0:
        description_es = None
    if contpt == 0:
        description_pt = None
    min_shipping_price = json_offer['min_shipping_price']
    min_shipping_price_additional = json_offer['min_shipping_price_additional']
    min_shipping_type = json_offer['min_shipping_type']
    min_shipping_zone = json_offer['min_shipping_zone']
    leadtime_to_ship = json_offer['leadtime_to_ship']
    logistic_class_code = json_offer['logistic_class']['code']
    logistic_class_label = json_offer['logistic_class']['label']
    print (min_shipping_price)
    print(min_shipping_price_additional)
    print(min_shipping_type)
    print(min_shipping_zone)
    print(leadtime_to_ship)
    print(logistic_class_code)
    print(logistic_class_label)
