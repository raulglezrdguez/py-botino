#!/bin/bash

myscript(){
    # python3 myscript [args..]
    cd /usr/www/
    python3 bot.py
}

until myscript; do
    echo "'bot.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done