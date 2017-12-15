#!/usr/bin/env python3
"""
init-db.py is the set-up script that has to be run before bot.py.
It generates


"""
import sys
import functions

size = int(sys.argv[1])

states = functions.generate_boards(size)

dictionary = functions.generate_database(states, 1000)

functions.save_json('db.json', dictionary)
