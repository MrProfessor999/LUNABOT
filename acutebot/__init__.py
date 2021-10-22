#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MIT License
# Copyright (c) 2020 Stɑrry Shivɑm // This file is part of AcuteBot
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os, sys, logging
from functools import wraps
from telegram.ext import Updater, Defaults
from telegram import ChatAction, ParseMode

TOKEN = "2095511325:AAGu4yvniqTs_vZ5s0YzH39jAqPlqshFLes"
WORKERS = "8"
TMDBAPI = "c7745c11"
DB_URI = "mongodb+srv://50:50@cluster0.hq9ev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
GENIUS = "false"
SPT_CLIENT_SECRET = a2f86375c76a408792c1e68082627db6"
SPT_CLIENT_ID = "4e27e02b549a4532adad9745d2212d14"
DEBUG = "false"
ARLTOKEN = "0b2d659e239b575f9cdac047a027ae88d5487069ab97a82861c4e0b71110072d62a9dcec4d2685481eb8c29604b374eaa5aa423ab494d00fac966e4fc45167f8499f3952eab45df7b72c3c340546ed858b4d60243d35fe9f9f1b5dbcba553302"
APP_URL = "https://acuterobot.herokuapp.com"
APIID = "7813081"
APIHASH = "deccd07c38a5ec9fa0fa6e58790fe292"


if logging.DEBUG:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )
else:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

__version__ = "1.1.3-rev09"

DEV_ID = 1329457821
LOG = logging.getLogger(__name__)

# Check python version:
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOG.info("You MUST need to have python version 3.6! shutting down...")
    sys.exit(1)


def typing(func):
    """Sends typing action while processing func command."""

    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_chat.id, action=ChatAction.TYPING
        )
        return func(update, context, *args, **kwargs)

    return command_func


# Use HTML treewide;
defaults = Defaults(parse_mode=ParseMode.HTML)
updater = Updater(TOKEN, use_context=True, workers=WORKERS, defaults=defaults)
dp = updater.dispatcher
