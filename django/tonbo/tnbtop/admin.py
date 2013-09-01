# -*- coding: utf8 -*-
#
# 管理画面のうんぬん

from django.contrib import admin
from tnbtop.models import Board
from tnbtop.models import Message

admin.site.register(Board)
admin.site.register(Message)
