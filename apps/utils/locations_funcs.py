import json

from django.core.cache import cache
import geoip2.database

reader = geoip2.database.Reader('GeoLite2/GeoLite2-City.mmdb')

'''
print("你查询的IP的地理位置是:")

print("地区：{}({})".format(response.continent.names["es"],
                         response.continent.names["zh-CN"]))

print("国家：{}({}) ，简称:{}".format(response.country.name,
                                response.country.names["zh-CN"],
                                response.country.iso_code))

print("洲／省：{}({})".format(response.subdivisions.most_specific.name,
                          response.subdivisions.most_specific.names["zh-CN"]))

print("城市：{}({})".format(response.city.name,
                         response.city.names["zh-CN"]))

print("经度：{}，纬度{}".format(response.location.longitude,
                          response.location.latitude))

print("时区：{}".format(response.location.time_zone))

print("邮编:{}".format(response.postal.code))
'''


class locationView(object):
    """
    :param ip
    descriptions: 通过IP地址获取到地理位置，使用了扩展GEOIP2
    :return
    """

    def get_locationInfoByIp(self, ip):
        values = cache.get(ip)
        if values is None:
            response = reader.city(ip)
            # city_name:城市名字
            city_name = response.continent.names["zh-CN"]
            return {'ip': ip, 'city_name': city_name}
        else:
            return values

    '''
    :param IP
    descriptions: 将通过IP查询到的城市名字，存入redis
    :return:
    '''

    def write_locationInfo_Into_redis(self, ip):
        city_data = self.get_locationInfoByIp(ip)
        # ip = city_data['ip']
        # city_name = city_data['city_name']
        cache.set(ip, city_data)
