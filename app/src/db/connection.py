#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import motor.motor_asyncio
from logger.log import new_logger

logger = new_logger("db")


USER = os.environ.get("JACARANDA_API_MONGO_USERNAME")
if USER is None:
    logger.critical("JACARANDA_API_MONGO_USERNAME is not set")
    raise ValueError("JACARANDA_API_MONGO_USERNAME is not set")

PASSWORD = os.environ.get("JACARANDA_API_MONGO_PASSWORD")
if PASSWORD is None:
    logger.critical("JACARANDA_API_MONGO_PASSWORD is not set")
    raise ValueError("JACARANDA_API_MONGO_PASSWORD is not set")

URL = os.environ.get("JACARANDA_API_MONGO_URL")
if URL is None:
    logger.critical("JACARANDA_API_MONGO_URL is not set")
    raise ValueError("JACARANDA_API_MONGO_URL is not set")
PORT = os.environ.get("JACARANDA_API_MONGO_PORT")
if PORT is None:
    logger.critical("JACARANDA_API_MONGO_PORT is not set")
    raise ValueError("JACARANDA_API_MONGO_PORT is not set")

client = motor.motor_asyncio.AsyncIOMotorClient(f"mongodb://{USER}:{PASSWORD}@{URL}:{PORT}/?authSource=admin")
db = client["jacaranda"]
