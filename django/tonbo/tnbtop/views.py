# -*- coding: utf8 -*-
#
# View 部分
#

from tnbtop.models import Board
from tnbtop.models import Message
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

def home(request):
    r""" 最近更新されたボード一覧を表示させる """

    data = dict(
        boards = Board.objects.all().order_by('-update_at')[:30]
    )
    return render_to_response('board/index.html', data)


def display (request, board_id):
    r""" ボードを表示させる """
    data = dict(
        board = get_object_or_404(Board, pk=board_id)
    )
    return render_to_response('board/detail.html', data,
                               context_instance=RequestContext(request))

def put (request, board_id):
    r""" ボードへ投稿 """
    pass

