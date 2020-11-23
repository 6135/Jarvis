import asyncio
import platform
import psutil
import os
import discord
import re
from datetime import datetime
from dotenv import load_dotenv
from dotenv.main import find_dotenv
from MiniGames import RPS, CoinFlip

class Jarvis(discord.Client):
	pass

load_dotenv(find_dotenv( ))
BOT_TOKEN = os.getenv("BOT_TOKEN")
Jarvis().run(BOT_TOKEN) 