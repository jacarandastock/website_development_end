#!/usr/bin/env python
# -*-coding:utf-8 -*-
from fastapi import APIRouter

router = APIRouter()

@router.get("/example")
async def index():
    return {"message": "Hello World"}
