# -*- coding: utf8 -*-
#
# View 部分
#
import logging

from tnbtop.models import Board
from tnbtop.models import Message
from django.template import Context
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# 表示件数（1件目を除く）
DISPLAY_LIMIT = 10

def index (request):
    return HttpResponseRedirect("/")

def home(request):
    r""" 最近更新されたボード一覧を表示させる """

    data = dict(
        boards = Board.objects.all().order_by('-update_at')
    )
    return render_to_response('board/index.html', data, context_instance=RequestContext(request))



def create (request):
    r""" 新規にボードを作成する """
    if request.method == "POST":
        board = Board(name=request.POST["name"])
        board.save()

        if board.id:
            message = Message(board=board, message_text=request.POST['message'], ipaddress=request.META["REMOTE_ADDR"], number=0)
            message.save()

        return HttpResponseRedirect("/board/{0}".format(board.id))

    return HttpResponseRedirect("/")


def display (request, board_id):
    r""" ボードを表示させる """
    board = get_object_or_404(Board, pk=board_id)
    message = Message.objects.filter(board=board).order_by('create_at')
    count   = message.count()
    data = dict(
        board = board,
        count = count,
        display_count = count
    )

    if len(message) > 0:
        get_ptr = 0

        # 10個以上メッセージがある時は、1件目を表示するが、
        # 10個までない場合は、全件表示
        if count > DISPLAY_LIMIT:
            get_ptr = count-DISPLAY_LIMIT
            data["top_message"] = message[0]
        data["messages"] = message[get_ptr:]
        data["display_count"] = count-get_ptr+1

    return render_to_response('board/detail.html', data,
                               context_instance=RequestContext(request))

def put (request, board_id):
    r""" ボードへ投稿 """
    board = get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
        messages = Message.objects.filter(board=board).order_by('create_at')
        count    = messages.count()

        if count >= 100:
            logging.warn("Board is over %d/100 in %d", count, board.id)
            return HttpResponseRedirect("/board/{0}".format(board.id))

        message = Message(board=board,
            message_text=request.POST['message'],
            ipaddress=request.META["REMOTE_ADDR"],
            number=count
        )

        message.save()

        if messages.count == 100:
            message = Message(board=board,
                message_text="100を越えました。もうこのボードは投稿することが出来ません",
                ipaddress=request.META["REMOTE_ADDR"],
                number=101
            )
            message.save()


    return HttpResponseRedirect("/board/{0}".format(board.id))

