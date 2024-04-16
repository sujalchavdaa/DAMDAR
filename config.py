#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6877953795:AAFJFiqqai5aYa4SZwLnNwNTDJOv3K-uwVA")
    API_ID = int(os.environ.get("API_ID", "23386496"))
    API_HASH = os.environ.get("API_HASH", "7b474ff5cd496bcb9071beaa863273fc")
    AUTH_USERS = "6338099703"

