import ujson
import struct
import _thread
import ubluetooth
from machine import Timer
from micropython import const

# python  ble recieve 
ble = ubluetooth.BLE()
ble.active(1)

def bt_irq(event, data):
    addr_type, addr, adv_type, rssi, adv_data = data
    mac = ''.join(['%02x' % b for b in bytes(addr)])
    if  mac == 'd0642309bd5c':
        res = {"rssi":rssi,"addr": mac}
        print("fuck!",res)
        
ble.irq(bt_irq)    
ble.gap_scan(0,10000,1000)
input()
