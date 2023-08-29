#!/usr/bin/python
# -*- coding: UTF-8 -*-

import asyncio
import websockets
import pathlib
import ssl
import objinfo

async def http():
    async with websockets.connect('ws://10.0.0.50:8013/ws') as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

    pass


async def https():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.load_verify_locations(pathlib.Path(__file__).with_name('1_games.com.cn.crt'))

    async with websockets.connect('wss://server50:8013/ws', ssl=ssl_context) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

    pass
























if __name__ == '__main__':
    print(u"测试输出")
    print(u"------------------------------------------------")
    # print(pathlib.Path(__file__).with_name('1_wtgames.com.cn.crt'))

    # asyncio.run(http())
    asyncio.run(https())
    
    # asyncio.get_event_loop().run_until_complete(http())
    # asyncio.get_event_loop().run_until_complete(https())


