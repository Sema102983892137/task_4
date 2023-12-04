# from django.core.mail import send_mail
from mysite.celery import app
# from student_testing.settings import DEFAULT_FROM_EMAIL
from datetime import datetime, timedelta
from .models import *
# from pytz import timezone

import logging

info_logger = logging.getLogger('information')
error_logger = logging.getLogger('errors')

logger = logging.getLogger(__name__)


# from django.

# @app.task(default_retry_delay=60, retry_kwargs={'max_retries': 10})
# def send_message(subject, message, recipient_list):
#     print("cacamba")
#     send_mail(subject=subject,
#               message=message,
#               from_email=DEFAULT_FROM_EMAIL,
#               recipient_list=recipient_list,
#               fail_silently=False)


@app.task
def send_time_message():
    all_reserve_slot = ReserveSlot.objects.all().select_related('slot').select_related('user')
    now = datetime.now()
    print(now)
    print(len(all_reserve_slot))
    for reserve_slot in all_reserve_slot:

        try:
            mydata = datetime.strptime(reserve_slot.slot.time, '%Y-%m-%d %H:%M:%S.%f')
            print(mydata)
            print(mydata - timedelta(hours=2))
            print(mydata <= now + timedelta(hours=2))
            if reserve_slot.is_one_day_notice == False and (mydata <= now + timedelta(hours=2)):
                info_logger.info(f"Уведомляю {reserve_slot.user.name} за 2 часа")


            print(mydata <= now + timedelta(days=1))
            if reserve_slot.is_one_day_notice == False and (mydata <= now + timedelta(days=1)):
                info_logger.info(f"Уведомляю {reserve_slot.user.name} за день")

        except Exception as e:
            print(e)

        # ex_end = test_ex.started_at + timedelta(minutes=test_ex.test_id.time_to_complete)
        # print(ex_end)
        # if now >= ex_end:
        #     TestExecution.objects.filter(id=test_ex.pk).update(status='timed_out', ended_at=now)
    # info_logger.info("loooooooooool")
