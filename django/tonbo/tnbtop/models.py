# -*- coding: utf8 -*-
#
# 掲示板モデル

from django.db import models

class Board (models.Model):
    r""" スレッドボード
    """
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__ (self):
        return self.name

class Message (models.Model):
    r""" 個々の投稿メッセージ
    """
    board = models.ForeignKey(Board)
    parent = models.ForeignKey("self", null=True, blank=True, default = None)
    message_text = models.TextField()
    ipaddress = models.IPAddressField()
    create_at = models.DateTimeField(auto_now=True)

    def __unicode__ (self):
        return self.message_text
