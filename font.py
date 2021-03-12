import binascii
def tohex(string):
    str_bin = string.encode('utf-8')
    return binascii.hexlify(str_bin).decode('utf-8')

fonts ={
    0xe68891:[0x06,0x0F,0x7C,0x0C,0x0C,0xFF,0x0C,0x0C,0x0F,0x0E,0x1C,0x7C,0x0C,0x0C,0x3F,0x18,
0x60,0x78,0x6C,0x6C,0x60,0xFF,0x60,0x66,0x66,0x6C,0x38,0x33,0x7B,0xCF,0x87,0x03],
    0xe788b1:[0x00,0x01,0x7F,0x33,0x19,0x7F,0x63,0xC3,0x7F,0x06,0x07,0x0F,0x19,0x30,0x63,0x1E
0x0C,0xFE,0x18,0x18,0xB0,0xFF,0x03,0x06,0xFC,0x00,0xF8,0x18,0xB0,0xE0,0xB8,0x0F],
    0xe5bca0:[0x80,0x8C,0x8C,0x98,0xB0,0xE0,0x80,0xFF,0xE0,0xB0,0xB0,0x98,0x8C,0xE6,0xC3,0x80],
    0xe69bbc:[0x00,0xF8,0x18,0xF8,0x18,0xF8,0x00,0xFE,0x66,0xFE,0x00,0xF8,0x30,0xE0,0x38,0x0F],
    0xe299a5:[0x00,0x00,0x22,0x43,0x5C,0x01,0x40,0x2A,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00]
    }


0x06,0x0F,0x7C,0x0C,0x0C,0xFF,0x0C,0x0C,0x0F,0x0E,0x1C,0x7C,0x0C,0x0C,0x3F,0x18
0x60,0x78,0x6C,0x6C,0x60,0xFF,0x60,0x66,0x66,0x6C,0x38,0x33,0x7B,0xCF,0x87,0x03/*"我",0*/

0x00,0x01,0x7F,0x33,0x19,0x7F,0x63,0xC3,0x7F,0x06,0x07,0x0F,0x19,0x30,0x63,0x1E
0x0C,0xFE,0x18,0x18,0xB0,0xFF,0x03,0x06,0xFC,0x00,0xF8,0x18,0xB0,0xE0,0xB8,0x0F/*"爱",1*/

0x01,0xFD,0x0D,0x0D,0x0D,0x7D,0x61,0x67,0x61,0x7D,0x0D,0x0D,0x0D,0x0D,0x79,0x31
0x80,0x8C,0x8C,0x98,0xB0,0xE0,0x80,0xFF,0xE0,0xB0,0xB0,0x98,0x8C,0xE6,0xC3,0x80/*"张",2*/

0x00,0x1F,0x18,0x1F,0x18,0x1F,0x00,0x7F,0x66,0x7F,0x00,0x3F,0x0C,0x07,0x1C,0xF0
0x00,0xF8,0x18,0xF8,0x18,0xF8,0x00,0xFE,0x66,0xFE,0x00,0xF8,0x30,0xE0,0x38,0x0F/*"曼",3*/
