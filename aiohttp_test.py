# -*- coding: utf-8 -*-
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('www.baidu.com')as resp:
        print(resp.status)
        print(await resp.text)