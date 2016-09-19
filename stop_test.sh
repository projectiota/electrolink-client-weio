#!/bin/bash

ps aux | grep python | grep test | awk '{print $2}' | xargs kill
