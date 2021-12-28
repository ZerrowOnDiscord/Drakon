from aiohttp.client import ClientSession
import sys, os, asyncio, random
from tasksio import TaskPool
from aiohttp import client_exceptions
from sys import exit
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Box

class ServerJoiner():
    async def joinServer(token, guildInv, bypassRuleScreen = False):
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

        tk = token
        try:
            tk = token[:25] + "*" * 34
        except:
            tk = "*" * len(token)

        randomProxy = ''
        if proxyless == False:
            randomProxy = proxies[random.randint(0, len(proxies)-1)]

        async with ClientSession(headers=headers) as session:
            try:
                async with session.post(f"https://discord.com/api/v9/invites/{guildInv}", proxy=randomProxy) as req:
                    if req.status == 429:
                        print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} is rate limited!")
                    else:
                        try:
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
                                elif 'banned' in json['message']:
                                    print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} is banned from the server!")
                                elif 'Maximum number of guilds reached' in json[
                                        'message']:
                                    print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} has 100 servers and couldn't join!")
                                else:
                                    print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} failed to join the server!")
                            else:
                                json = await req.json()
                                print(Colors.white + "[" + Colors.green + "+" + Colors.white + f"] {tk} joined the server!")
                                if bypassRuleScreen == True:
                                    async with session.get("https://discord.com/api/v9/guilds/"+json['guild']['id']+"/member-verification?with_guild=false&invite_code=" + guildInv) as req2:
                                        if req2.status == 200:
                                            j = await req2.json()
                                            async with session.put("https://discord.com/api/v9/guilds/"+json['guild']['id']+"/requests/@me", json=j) as req3:
                                                if req3.status == 201:
                                                    print(Colors.white + "[" + Colors.green + "+" + Colors.white + f"] {tk} bypassed rules screen!")
                                                else:
                                                    print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} failed to bypass rules screen!")
                                        else:
                                            print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} failed to bypass rules screen!")
                        except client_exceptions.ContentTypeError:
                            pass
            except client_exceptions.ClientHttpProxyError:
                print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} failed to join the server, Proxy Error!")
                pass
            except client_exceptions.ClientConnectorError:
                print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] {tk} failed to join the server, Failed to connect to discord.com!")
                pass