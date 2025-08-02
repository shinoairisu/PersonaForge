import os
from typing import Tuple
from pathlib import Path
from enum import Enum

import yaml
from pprint import pprint

FOLDER = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(FOLDER, "config.yaml")


def load_config() -> dict:
    """
    读只读一次
    :return:
    """
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def update_config():
    pass


def load_apikey(domain, name) -> Tuple[str, str]:
    """
    从内存模型中读取apikey和url
    domain就是类似openai
    :return:
    """
    pass


def modify_apikey(domain, name, url, key):
    """
    修改apikey
    一旦修改就会修改内存模型，然后写出。不会多次读
    """
    pass

def list_config():
    """会直接打出内存模型"""
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        print(f.read())

config = load_config()