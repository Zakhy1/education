import logging
import traceback

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from courses.models import Course

logger = logging.getLogger('django')


class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.error(traceback.format_exc())
            return render(request, 'error.html', status=400)

        if isinstance(response, (dict, list)):
            return self._response(response)
        else:
            return response
