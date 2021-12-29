from aiohttp.client import ClientSession
import sys, os, asyncio, random
from tasksio import TaskPool
from aiohttp import client_exceptions
from sys import exit
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Box

class Report():
    async def report(token, channel_id, guild_id, message_id, reason):
        tokens = []
        for token in open("files/tokens.txt"):
            if token != '':
                tokens.append(
                    token.replace("\n", "").replace('\r\n',
                                                    '').replace('\r', ''))
        # Proxy Support
        proxies = []
        proxyless = True
        for proxy in open("files/proxies.txt"):
                if proxy != '':
                    split = proxy.replace("\n", "").replace('\r\n',
                                                    '').replace('\r', '').split(":")
                    if len(split) == 2:
                        proxies.append(f"http://{split[0]}:{split[1]}")
                    elif len(split) == 4:
                        proxies.append(f"http://{split[2]}:{split[3]}@{split[0]}:{split[1]}")

        # Proxy Support
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        payload = {'channel_id':channel_id, 
        'guild_id':guild_id, 
        'message_id':message_id, 
        'reason':reason}

        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        randomProxy = ''
        if proxyless == False:
            randomProxy = proxies[random.randint(0, len(proxies)-1)]

        async with ClientSession(headers=headers) as session:
            async with session.post(
                    "https://discord.com/api/v6/report" , proxy=randomProxy, json=payload) as req:
                if r.status_code == 201:
                    print(Colors.white + "[" + Colors.green + "+" + Colors.white + f"] {tk} Reported!")
                else:
                    if r.status_code == 401:
                        print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} Token phonelocked!")
                    else:
                        log(str(r.content) + ' ' + str(r.status_code))
                if req.status == 429:
                    print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} is rate limited!")
                elif req.status == 204:
                    print(Colors.white + "[" + Colors.green + "+" + Colors.white + f"] {tk} left the server!")
                else:
                    json = await req.json()
                    if 'message' in json:
                        if 'verify' in json['message']:
                            print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} is unverified and removed from list!")
                            if token in tokens:
                                tokens.remove(token)
                        elif 'Unauthorized' in json['message']:
                            print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} is not a real token and removed from list!")
                            if token in tokens:
                                tokens.remove(token)
                        else:
                            print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} failed to report!")