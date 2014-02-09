#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gjms.users

fritz = gjms.users.add("Fritz", "yolo#2014", "fritz@fratz.at")
print "%s | %s | %s " % (fritz.name, fritz.password, fritz.email)

gjms.users.delete("Fritz")