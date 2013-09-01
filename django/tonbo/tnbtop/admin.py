# -*- coding: utf8 -*-
#
# 管理画面のうんぬん

from django.contrib import admin
from tnbtop.models import Board
from tnbtop.models import Message


class MessageInline(admin.StackedInline):
    model = Message
    extra = 1

class BoardAdmin(admin.ModelAdmin):
    fieldsets = [
        ('板名',   {'fields': ['name']}),
        # ('作成日', {'fields': ['create_at']}),
    ]
    inlines = [MessageInline]

admin.site.register(Board, BoardAdmin)
admin.site.register(Message)
