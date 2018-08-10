# -*- coding: utf-8 -*-
from datetime import datetime
class flattest():

    def time_tip(self):
        now_time = datetime.now()
        time_str = datetime.strftime(now_time, '%S%M%H%d%m%g')
        self.time_hex = ''
        for i in range(0, len(time_str), 2):
            tip = hex(int(time_str[i:i + 2]))[2:].rjust(2, '0')
            self.time_hex += tip

    import binascii
    def data_deal(self):
        startSign='4040BB000001'   # 启动符2、流水号2、版本号2  6
        sendtime = self.time_hex   # =时间标签6
        oriaddr = '010000000000 '  # 源地址6
        desaddr = '000000000000 '  # 目的地址6
        datalen = ''  # 应用单元数据长度2
        combyte = '02' # 命令字节1
        typetip = self.device_type  # 类型标志1
        infonum = '01'  #信息对象数目、信息体
        intobody='' #
        buildtime='' #时间标签
        enddata =   # 结束符
        print(type(startSign))


ceshi=flattest()
ceshi.data_deal()