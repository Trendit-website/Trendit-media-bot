'''
This module defines the configuration settings for the Trendit³ Bot

@author: Emmanuel Olowu
@link: https://github.com/zeddyemy
@package: Trendit³
'''
import os, secrets, logging
from typing import Final
from datetime import timedelta


# Configure the logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class BaseConfig:
    DEBUG = False
    ENV = os.environ.get('ENV') or 'development'
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
    EMERGENCY_MODE = os.environ.get('EMERGENCY_MODE') or False
    
    API_DOMAIN_NAME = os.environ.get('API_DOMAIN_NAME') or 'https://api.trendit3.com'
    TELEGRAM_BOT_TOKEN: Final = os.environ.get("TELEGRAM_BOT_TOKEN")
    BOT_USERNAME: Final = "@Trendit3Bot"
    BOT_APP_USERNAME = "Trendit3Bot"
    BOT_PASSWORD: Final = os.environ.get("BOT_PASSWORD") or "TrenditBot1"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    
    APP_DOMAIN_NAME = os.environ.get('APP_DOMAIN_NAME') or 'https://staging.trendit3.com'
    API_DOMAIN_NAME = os.environ.get('API_DOMAIN_NAME') or 'https://api-staging.trendit3.com'

class ProductionConfig(BaseConfig):
    DEBUG = False
    
    APP_DOMAIN_NAME = os.environ.get('APP_DOMAIN_NAME') or 'https://app.trendit3.com'
    API_DOMAIN_NAME = os.environ.get('API_DOMAIN_NAME') or 'https://api.trendit3.com'

# Map config based on environment
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}

config_class =  DevelopmentConfig if BaseConfig.ENV == "development" else ProductionConfig

class Config(DevelopmentConfig if BaseConfig.ENV == "development" else ProductionConfig):
    CONFIG_CLASS = config_class