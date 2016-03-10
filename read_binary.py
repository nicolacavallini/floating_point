import struct

def single_precision(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('>f', num))

def double_precision(num):
    return ''.join(bin(ord(c)).replace('0b', '').rjust(8, '0') for c in struct.pack('>d', num))
    
def split_single(b32):

    print('number of bits = '+str(len(b32)))

    sbit, wbits, pbits = b32[:1], b32[1:9], b32[9:]

    print('binary sign = '+sbit)
    print('binary exponent = '+wbits)
    print('binary mantissa = ' +pbits)
    
    return sbit, wbits, pbits

def split_double(b64):
    print('number of bits = '+str(len(b64)))

    sbit, wbits, pbits = b64[:1], b64[1:12], b64[12:]

    print('binary sign = '+sbit)
    print('binary exponent = '+wbits)
    print('binary mantissa = ' +pbits)
    return sbit, wbits, pbits
