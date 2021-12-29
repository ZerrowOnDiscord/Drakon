import asyncio
import aiosonic
import re
import os
import time
import threading
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Box
from tasksio import TaskPool


class RequestTimeout:
    request_timeout = 100
    sock_read = 100
    sock_connect = 100

TOKENS_LOADED = 0
TOKENS_INVALID = 0
TOKENS_LOCKED = 0
TOKENS_VALID = 0
TOKENS_VALID_LIST = []

def filter_tokens(unfiltered):
    tokens = []
    
    for line in [x.strip() for x in unfiltered.readlines() if x.strip()]:
        for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
            for token in re.findall(regex, line):
                if token not in tokens:
                    tokens.append(token)
                
    return tokens

async def check(token, client):
    global TOKENS_INVALID, TOKENS_LOCKED, TOKENS_VALID, TOKENS_VALID_LIST
    
    response = await client.get("https://discord.com/api/v9/users/@me/library", headers={
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
    }, timeouts=RequestTimeout)

    tk = token
    try:
        tk = token[:25] + "*" * 34
    except:
        tk = "*" * len(token)
    
    if response.status_code == 200:
        TOKENS_VALID += 1
        TOKENS_VALID_LIST.append(token)
        print(Colors.white + "[" + Colors.green + "+" + Colors.white + f"] [VALID] {tk}")
            
    elif response.status_code == 401:      
        TOKENS_INVALID += 1
        print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] [INVALID] {tk}")
        
    elif response.status_code == 403:
        TOKENS_LOCKED += 1
        print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] [LOCKED] {tk}")
    
async def checker():
    global TOKENS_INVALID, TOKENS_LOCKED, TOKENS_VALID, TOKENS_LOADED, TOKENS_VALID_LIST
    
    client = aiosonic.HTTPClient()
    
    try:
        with open('files/tokens.txt', 'r') as tokens:
            filtered = filter_tokens(tokens)
            TOKENS_LOADED = len(filtered)
            async with TaskPool(100) as pool:
                for token in filtered:
                    await pool.put(check(token, client))
                    
            await client.shutdown()

            print(Colors.white + "[" + Colors.green + "+" + Colors.white + f"] Tokens Loaded: {TOKENS_LOADED} \n| Valid: {TOKENS_VALID} \n| Locked: {TOKENS_LOCKED} \n| Invalid: {TOKENS_INVALID}") 
            
            with open(f'files/working.txt', 'w') as handle:
                handle.write('\n'.join(TOKENS_VALID_LIST))
                handle.close()
                
            print(Colors.white + "[" + Colors.green + "+" + Colors.white + f"] Saved to working.txt.")
                      
    except Exception as e:
        print(e)
        print(Colors.white + "[" + Colors.red + "x" + Colors.white + f"] Can't open tokens.txt.")