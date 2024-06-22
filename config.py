'''
This module defines the configuration settings for the Trendit³ Bot

@author: Emmanuel Olowu
@link: https://github.com/zeddyemy
@package: Trendit³
'''
import os, secrets, logging
from typing import Final
from datetime import timedelta



class Config:
    ENV = os.environ.get('ENV') or 'development'
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    EMERGENCY_MODE = os.environ.get('EMERGENCY_MODE') or False
    
    API_DOMAIN_NAME = os.environ.get('API_DOMAIN_NAME') or 'https://api.trendit3.com'
    TELEGRAM_BOT_TOKEN: Final = os.environ.get("TELEGRAM_BOT_TOKEN")
    BOT_USERNAME: Final = "@Trendit3Bot"
    