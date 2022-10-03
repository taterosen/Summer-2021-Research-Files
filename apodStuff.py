#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 08:54:57 2021

@author: taterosen
"""

import apod_object_parser as aop

response = aop.get_data("tbGHwnYGeyNA0FTsnTgOyFExRD78c8pMv1p6Asje")

date = aop.get_date(response)
title = aop.get_title(response)
url = aop.get_url(response)
expl = aop.get_explaination(response)

print(date)
print(title)
print(expl)
print(url)