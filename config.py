#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6435076222:AAG3Ock7QYUWLQ1pK2OrQEFE8KKNbomGn7w")
    API_ID = int(os.environ.get("API_ID", "23221988"))
    API_HASH = os.environ.get("API_HASH", "dd967cb284dcf265894c2445fdf63f06")
    AUTH_USERS = "6607659765"

