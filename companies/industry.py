import json

with open('GICS.json') as jsonFile:
    INDUSTRIES_DICT = json.load(jsonFile)

SECTORS = {}
INDUSTRY_GROUPS = {}
INDUSTRIES = {}
for sector_code, sector in INDUSTRIES_DICT.items():
    SECTORS[sector_code] = sector['name']
    for industry_group_code, industry_group in sector['industry_groups'].items():
        INDUSTRY_GROUPS[industry_group_code] = industry_group['name']
        for industry_code, industry in industry_group['industries'].items():
            INDUSTRIES[industry_code] = industry['name']

INDUSTRY_CHOICES = [(industry_group,
                     tuple((code, name) for code, name in INDUSTRIES.items()
                           if code[:4] == industry_group_code))
                    for industry_group_code, industry_group in INDUSTRY_GROUPS.items()]
