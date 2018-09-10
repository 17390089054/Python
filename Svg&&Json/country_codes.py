from pygal_maps_world.i18n import COUNTRIES
def get_country_code(country_name):
    #根据指定的国家,返回Pygal使用的两个字母的国别吗
    for code,name in COUNTRIES.items():
        if name==country_name:
            return code
    #如果没有找到指定的国家就返回NOne
    return None
