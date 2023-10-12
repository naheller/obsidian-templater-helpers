#!/usr/bin/env python3

import sys
from time import sleep
from os import listdir
from os.path import isfile, join
from re import match

# supply path via Templater user function definition: <path>/obs_todo_migr.py <% tp.file.folder(true) %>
daily_notes_dir = sys.argv[1]

prevnote = []
open_todos = []
unchecked = "- [ ]"

files = [f for f in listdir(daily_notes_dir) if isfile(join(daily_notes_dir, f))]

if len(files) >= 2:
    files.sort(reverse=True)
    prevfile = files[1] # need second newest file since new note exists when this is called

    # grab unchecked todos to move to new day
    start_reading = False

    with open(daily_notes_dir+"/"+prevfile, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if '##### *Today*' in line:
                start_reading = True
                continue
            if start_reading and line.strip() is "":
                break
            if start_reading and unchecked in line:
                open_todos.append(line)

    for todo in open_todos:
        print(todo[:-1])
else:
    print('- [ ]')
