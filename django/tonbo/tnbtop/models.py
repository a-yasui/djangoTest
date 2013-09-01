# -*- coding: utf8 -*-
#
# 掲示板モデル

from django.db import models

class Board (models.Model):
    r""" スレッドボード
    """
    name = models.CharField(max_length=200, verbose_name="スレッドボード名")
    create_at = models.DateTimeField(auto_now=True, verbose_name="作成日付")
    update_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__ (self):
        return self.name

class Message (models.Model):
    r""" 個々の投稿メッセージ
    """
    board = models.ForeignKey(Board)
    parent = models.ForeignKey("self", null=True, blank=True, default = None, verbose_name="レス先")
    number       = models.IntegerField(max_length=102, default=0, verbose_name='投稿番号')
    message_text = models.TextField(verbose_name="メッセージ")
    ipaddress = models.IPAddressField(verbose_name='投稿者IP')
    create_at = models.DateTimeField(auto_now=True, verbose_name="投稿日付")

    def __unicode__ (self):
        return self.message_text
