import sys 
import os
from pystyle import Center, Colors, Colorate
import time
import asyncio
from tasksio import TaskPool
import threading
import discord
import requests
sys.path.append('methods')
os.system(f'title [Drakon] - Loading...')
os.system('cls' if os.name == 'nt' else 'clear')
from joiner import ServerJoiner
print(f"{Colors.white}[{Colors.purple}+{Colors.white}] Joiner method loaded.")
from leaver import ServerLeaver
print(f"{Colors.white}[{Colors.purple}+{Colors.white}] Leaver method loaded.")
from channelspammer import ChannelSpammer
print(f"{Colors.white}[{Colors.purple}+{Colors.white}] ChannelSpammer method loaded.")
from dmspammer import DMSpammer
print(f"{Colors.white}[{Colors.purple}+{Colors.white}] DMSpammer method loaded.")
from biochanger import BioChanger
print(f"{Colors.white}[{Colors.purple}+{Colors.white}] BioChanger method loaded.")
from webhook import WebhookSpammer
print(f"{Colors.white}[{Colors.purple}+{Colors.white}] WebhookSpammer method loaded.")
from reaction import ReactionSpammer
print(f"{Colors.white}[{Colors.purple}+{Colors.white}] ReactionSpammer method loaded.")
from report import Report
print(f"{Colors.white}[{Colors.purple}+{Colors.white}] Report method loaded.")
time.sleep(1)

### Ne pas toucher !!!!
version = 1.1

### Banner
banner = """
 /$$$$$$$                     /$$                          
| $$__  $$                   | $$                          
| $$  \ $$  /$$$$$$  /$$$$$$ | $$   /$$  /$$$$$$  /$$$$$$$ 
| $$  | $$ /$$__  $$|____  $$| $$  /$$/ /$$__  $$| $$__  $$
| $$  | $$| $$  \__/ /$$$$$$$| $$$$$$/ | $$  \ $$| $$  \ $$
| $$  | $$| $$      /$$__  $$| $$_  $$ | $$  | $$| $$  | $$
| $$$$$$$/| $$     |  $$$$$$$| $$ \  $$|  $$$$$$/| $$  | $$
|_______/ |__/      \_______/|__/  \__/ \______/ |__/  |__/
"""
### Header
def headofprogram():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.purple_to_blue, banner, 1))
    print(" ")
    print(Colorate.Horizontal(Colors.purple_to_blue, "╔══════════════════════════", 1))
    print(Colorate.Horizontal(Colors.purple_to_blue, "║    Made with ", 1) + Colors.red + "♥")
    print(Colorate.Horizontal(Colors.purple_to_blue, "║    By Zerrow", 1))
    print(Colorate.Horizontal(Colors.purple_to_blue, "╚══════════════════════════", 1))
    print(" ")
### Updater
def updater():
    lastversion = 'https://pastebin.com/raw/bvyhZHQC' 
    r = requests.get(lastversion)
    lastversion = float(r.text)
    if version < lastversion:
        os.system(f'title [Drakon] - New Update!')
        headofprogram()
        print(Colorate.Horizontal(Colors.purple_to_blue, ">> Une nouvelle mise a jour est disponnible !", 1))
        choice = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] La download [y/n] → ", 1))
        if choice == "y":
            print(Colorate.Horizontal(Colors.purple_to_blue, "[!] Download... ", 1))
            path = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez indiquer le chemin de telechargement de la nouvelle version → ", 1))
            system(f"""cd {path} && powershell -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/ZerrowOnDiscord/Drakon/archive/refs/heads/main.zip', 'drakon-main.zip')""")
            print(Colorate.Horizontal(Colors.purple_to_blue, "[>] Downloaded ! ", 1))
        if choice == "n":
            loop = asyncio.get_event_loop()
            loop.run_until_complete(Start.start())
    else:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(Start.start())
### Start
class Start:
    async def start():
        os.system(f'title [Drakon] - Choose your method')
        headofprogram()
        print(Colorate.Horizontal(Colors.purple_to_blue, "╔══════════════════════════", 1))
        print(Colorate.Horizontal(Colors.purple_to_blue, "║    [>] ", 1) + Colors.white + "Methods:")
        print(Colorate.Horizontal(Colors.purple_to_blue, "║    [>] ", 1) + Colors.white + ".joiner")
        print(Colorate.Horizontal(Colors.purple_to_blue, "║    [>] ", 1) + Colors.white + ".leaver")
        print(Colorate.Horizontal(Colors.purple_to_blue, "║    [>] ", 1) + Colors.white + ".channel_spammer")
        print(Colorate.Horizontal(Colors.purple_to_blue, "║    [>] ", 1) + Colors.white + ".dm_spammer")
        print(Colorate.Horizontal(Colors.purple_to_blue, "║    [>] ", 1) + Colors.white + ".bio_changer")
        print(Colorate.Horizontal(Colors.purple_to_blue, "║    [>] ", 1) + Colors.white + ".Webhook_spammer")
        print(Colorate.Horizontal(Colors.purple_to_blue, "║    [>] ", 1) + Colors.white + ".reaction_spammer")
        print(Colorate.Horizontal(Colors.purple_to_blue, "║    [>] ", 1) + Colors.white + ".mass_report")
        print(Colorate.Horizontal(Colors.purple_to_blue, "╚══════════════════════════", 1))
        method = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Entrez une commande → ", 1))
        if method == ".joiner":
            os.system(f'title [Drakon] - Method: Joiner')
            await Methods.joiner()
        if method == ".leaver":
            os.system(f'title [Drakon] - Method: Leaver')
            await Methods.leaver()
        if method == ".channel_spammer":
            os.system(f'title [Drakon] - Method: ChannelSpammer')
            await Methods.channelspammer()
        if method == ".dm_spammer":
            os.system(f'title [Drakon] - Method: DMSpammer')
            await Methods.dmspammer()
        if method == ".bio_changer":
            os.system(f'title [Drakon] - Method: BioChanger')
            await Methods.biochanger()
        if method == ".webhook_spammer":
            os.system(f'title [Drakon] - Method: WebhookSpammer')
            await Methods.webhookspammer()
        if method == ".reaction_spammer":
            os.system(f'title [Drakon] - Method: ReactionSpammer')
            await Methods.reactionspammer()
        if method == ".mass_report":
            os.system(f'title [Drakon] - Method: MassReport')
            await Methods.report()
            
class Methods:
    async def joiner():
        tokens = []
        for token in open("files/tokens.txt"):
            tokens.append(token.replace("\n", "").replace('\r\n','').replace('\r', ''))
        guildInv = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Entrez l'invitation du serveur → ", 1))
        bypassRulesScreen = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Voulez vous utiliser la bypass method? [Y/N] → ", 1))
        if bypassRulesScreen.lower() == 'y':
            bypassRulesScreen = True
        else:
            bypassRulesScreen = False
        if 'discord.gg' in guildInv or 'discord.com' in guildInv:
            guildInv = guildInv.replace('https://discord.com/invite/','').replace('https://discord.gg/','').replace('discord.gg/', '')
        async with TaskPool(5_000) as pool:
            for token in tokens:
                await pool.put(ServerJoiner.joinServer(token, guildInv, bypassRulesScreen))
        time.sleep(4)
        await Start.start()
    async def leaver():
        tokens = []
        for token in open("files/tokens.txt"):
            tokens.append(token.replace("\n", "").replace('\r\n','').replace('\r', ''))
        guildId = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Entrez l'ID du serveur → ", 1))
        if guildId == '0':
            await Start.start()
        async with TaskPool(5_000) as pool:
            for token in tokens:
                await pool.put(ServerLeaver.leaveServer(token, guildId))
        time.sleep(4)
        await Start.start()
    async def channelspammer():
        tokens = []
        for token in open("files/tokens.txt"):
            tokens.append(token.replace("\n", "").replace('\r\n','').replace('\r', ''))
        chId = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'ID du channel → ", 1))
        if chId == '0':
            await Start.start()
        msg = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir le message → ", 1))
        if msg == '0':
            await Start.start()
        amount = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir le nombre → ", 1))
        if amount == '0':
            await Start.start()
        replyQues = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Repondre a un message? [Y/N] → ", 1))
        replyMsg = None
        if replyQues.lower() == 'y':
            replyMsg = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'ID du message a repondre → ", 1))
        numberQues = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Mettre une suite aleatoire dans le debut du message (conseille)? [Y/N] → ", 1))
        numberAft = False
        if numberQues.lower() == 'y':
            numberAft = True
        async with TaskPool(5_000) as pool:
            for token in tokens:
                await pool.put(ChannelSpammer.channelSpammer(token, chId, msg, amount, replyMsg, numberAft))
        time.sleep(4)
        await Start.start()
    async def dmspammer():
        tokens = []
        for token in open("files/tokens.txt"):
            tokens.append(token.replace("\n", "").replace('\r\n','').replace('\r', ''))
        userId = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'ID de l'utilisateur → ", 1))
        if userId == '0':
            await Start.start()
        msg = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir le message → ", 1))
        if msg == '0':
            await Start.start()
        amount = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir le nombre → ", 1))
        if amount == '0':
            await Start.start()
        async with TaskPool(5_000) as pool:
            for token in tokens:
                await pool.put(DMSpammer.dmSpammer(token, userId, msg, amount))
        time.sleep(4)
        await Start.start()
    async def biochanger():
        tokens = []
        for token in open("files/tokens.txt"):
            tokens.append(token.replace("\n", "").replace('\r\n','').replace('\r', ''))
        bio = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir la nouvelle bio → ", 1))
        if bio == '0':
            await Start.start()
        async with TaskPool(5_000) as pool:
            for token in tokens:
                await pool.put(BioChanger.bioChanger(token, bio))
        time.sleep(4)
        await Start.start()
    async def webhookspammer():
        webhookUrl = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'URL du Webhook → ", 1))
        if webhookUrl == '0':
            await Start.start()
        msg = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir le message → ", 1))
        if msg == '0':
            await Start.start()
        amount = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir le nombre → ", 1))
        async with TaskPool(5_000) as pool:
            for i in range(int(amount)):
                await pool.put(WebhookSpammer.webhookSpammer(webhookUrl, msg))
        time.sleep(4)
        await Start.start()
    async def reactionspammer():
        tokens = []
        for token in open("files/tokens.txt"):
            tokens.append(token.replace("\n", "").replace('\r\n','').replace('\r', ''))
        chId = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'ID du channel → ", 1))
        if chId == '0':
            await Start.start()
        msgId = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'ID du message → ", 1))
        if msgId == '0':
            await Start.start()
        emoji = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'emoji (seulement pour les emojis perso, a utiliser comme ceci: name:id)' → ", 1))
        if emoji == '0':
            await Start.start()
        async with TaskPool(5_000) as pool:
            for token in tokens:
                await pool.put(ReactionSpammer.reactionSpammer(token, chId, msgId, emoji))
        time.sleep(4)
        await Start.start()
    async def report():
        tokens = []
        for token in open("files/tokens.txt"):
                tokens.append(
                    token.replace("\n", "").replace('\r\n','').replace('\r', ''))
        print('\n| REPORT REASONS\n| 1: Illegal content\n| 2: Harrassment\n| 3: Spam or Phishing Links\n| 4: Self harm\n| 5: NSFW Content\n')
        chId = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'ID du channel → ", 1))
        if chId == '0':
            await Start.start()
        msgId = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'ID du message → ", 1))
        if msgId == '0':
            await Start.start()
        gId = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'ID du serveur → ", 1))
        if gId == '0':
            await Start.start()
        reason = input(Colorate.Horizontal(Colors.purple_to_blue, "[>] Veuillez fournir l'ID du serveur → ", 1))
        if gId == '0':
            await Start.start()
        reason = str(int(reason) - 1)
        async with TaskPool(5_000) as pool:
            for token in tokens:
                await pool.put(Report.report(token, chId, gId, msgId))
        time.sleep(4)
        await Start.start()

updater()