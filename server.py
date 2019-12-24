from ctypes import *
from enum import Enum
import winreg
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class UserChannel(Enum):
    UTC = 0
    BSP = 1
    AWA = 2
    AWS = 3
    TWA = 4
    TWS = 5
    TWD = 6
    COURSE = 9
    LWY = 10
    SET = 11
    DRIFT = 12
    HDG = 13
    BARO = 16
    VMG = 31
    GPSQ = 39
    HDOP = 40
    PDOP = 41
    VDOP = 42
    GPSN = 43
    GPSA = 44
    GPSM = 47
    LAT = 48
    LON = 49
    COG = 50
    SOG = 51


REG_PATH = 'SOFTWARE\Expedition\Core'
def get_dll_location():
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, 'Location')
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None
dll_location = get_dll_location()
    
class ChannelRequestHandler(BaseHTTPRequestHandler):
    expedition = windll.LoadLibrary(dll_location +'\ExpDLL.dll')

    def get_value(self, user_channel, boat_id): 
        result = c_double(0)
        self.expedition.GetExpVar(c_short(user_channel.value), pointer(result), c_short(boat_id), pointer(c_short(user_channel.value)))
        return result.value

    def get_all_values(self, boat_id):
        results = {}
        for channel in UserChannel:
            results[channel.name] = self.get_value(channel, boat_id)
        return results

    def do_GET(self):
        print(parse_qs(urlparse(self.path)[4]))
        params = parse_qs(urlparse(self.path)[4])
        boat_id = 0
        if 'boat_id' in params:
            boat_id = params['boat_id'][0]
        self.send_response(200)
        results = json.dumps(self.get_all_values(boat_id))
        self.end_headers()
        self.wfile.write(str.encode(results))

PORT = 8080
httpd = HTTPServer(('localhost', PORT), ChannelRequestHandler)
httpd.serve_forever()



