# -*- coding: utf8 -*-
#
# View 部分
#

from django.http import HttpResponse

def home(request):
    return HttpResponse("You're welcome")

