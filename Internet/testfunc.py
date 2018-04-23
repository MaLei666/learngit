import random
def uchar_checksum(data, byteorder='little'):
    ''''' 
    char_checksum 按字节计算校验和。每个字节被翻译为无符号整数 
    @param data: 字节串 
    @param byteorder: 大/小端 
    '''
    length = len(data)
    checksum = 0
    for i in range(0, length):
        checksum += int.from_bytes(data[i:i + 1], byteorder, signed=False)
        #checksum &= 0xFF  # 强制截断

    return checksum

data1=bytes(b'\x01\x7F\xFF')


print(uchar_checksum(data1))