#!/usr/bin/env bash
# -*- coding: utf-8 -*-


python manage.py makemigrations && \
python manage.py migrate
