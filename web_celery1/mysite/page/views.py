from django.shortcuts import render
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.db.models import F
from .tasks import *
import datetime

info_logger = logging.getLogger('information')
error_logger = logging.getLogger('errors')

logger = logging.getLogger(__name__)


class FullAnswer:
    def __init__(self, data=None, error=None):
        if data is not None:
            self.answer = {
                'status': "success",
                'meta': None,
                'error': None,
                'data': data}
        else:
            self.answer = {
                'status': "failure",
                'meta': None,
                'error': error,
                'data': None}


def my_error(log_message, error):
    error_logger.error(log_message)
    my_answer = FullAnswer(error=error)
    return Response(my_answer.answer)


class MyAPIView(APIView):  # 3
    def is_not_used(self):
        pass

    def post(self, request):
        self.is_not_used()
        try:
            user_id = request.data['user_id']
            user = MyUser.objects.get(pk=user_id)
            doctor_id = request.data['doctor_id']
            slot_time = request.data['slot']

            doc = MyDoctor.objects.filter(pk=doctor_id).first()
            print(doc)
            slot = Slot.objects.get(doctor=doc, time=slot_time)
            print(slot)
            reserv = ReserveSlot.objects.filter(slot=slot)
            print(reserv)
            if len(reserv):
                raise Exception
            print("ok")
            ReserveSlot(slot=slot, user=user).save()
            return Response({"ok": "ok"})
        except Exception as e:
            print("scjnds,cn,sdncsdncknskjcnksdnckjnsdc")
            print(e)
            return Response({"Ты": "не твори говно"})


"""

{"user_id":1,
"doctor_id":1,
"slot":"2023-12-4 19:35:49.557359"}

"""
