#!/usr/bin/env python3
'''a coroutine called async_comprehension that takes no arguments.
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''coroutine will collect 10 random numbers using an  async_generator.
    '''
    return [num async for num in async_generator()]
