#-*- coding: utf-8 -*-

"""URL映射"""

from django.views.generic.base import View
from django.http import HttpResponse
from django.shortcuts import render
from jiaxiao.config import site_name, channels, theme

class URLDispatchView(View):
    """URL映射"""

    def get(self, request, page_name=''):
        """URL GET"""

        if page_name == '':
            page_name = 'index'
        template_name = '%s/%s.html' % (theme, page_name)
        #return HttpResponse(page_name)
        return render(request, template_name, {
            'site_name': site_name,
            'channels': channels,
        })