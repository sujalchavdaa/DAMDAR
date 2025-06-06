#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7855577752:AAFKQfqK9SOlQxPE5NPJrJrPFK6xjXOFZ8Y")
    API_ID = int(os.environ.get("API_ID", "26330942"))
    API_HASH = os.environ.get("API_HASH", "5de9fd033aa828dfd3bf0c28adeee660")
    AUTH_USERS = "6883471516"

