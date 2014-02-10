#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gjms.users

example = gjms.users.add("user", "password", "username@example.com")
print "%s | %s | %s " % (example.name, example.password, example.email)

gjms.users.delete("user")
