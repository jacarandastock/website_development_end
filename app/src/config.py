#!/usr/bin/env python

# -*-coding:utf-8 -*-
import os

# app_env = os.environ.get("APP_ENV", "prod")
app_env = os.environ.get("APP_ENV", "dev")  # todo 暂时默认为dev, 以后改为prod

# dev 模式下debug为True
debug = (app_env == "dev")