import logging
import unittest

from app_testing.file import File
from app_testing.client import Client
from app_testing.device import Device
from app_testing.schedule import Schedule

class TestSchedule(unittest.TestCase):
    def test_selectDeviceForSchedule(self):
        schedule = Schedule()
        schedule.selectDeviceForSchedule()
        time,exc=schedule.scheduleTime()
        # time, exc = schedule.nowTime()
        response=schedule.makeSchedule()
        print("2: ", time, exc)
        print("3: ", response.json())




