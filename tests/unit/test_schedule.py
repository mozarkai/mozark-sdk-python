from unittest import TestCase

from app_testing.schedule import  Schedule
from app_testing.executetest import TestExecute

class TestSchedule(TestCase):
    def test_schedule_initialize(self):
        start_time = None
        devices = ["abc", "xyz"]
        test_configuration = {"captureCPUMetrics": True, "captureLiveLogs" : True}
        test_configuration.CAPTURE_CPU_METRICS = True

        schedule = Schedule()
        schedule.set_devices(devices=devices)
        schedule.set_test_configuration(test_configuration=test_configuration)

        execute_test = TestExecute() # user API
        execute_test.execute_now(schedule=schedule) # user API
        execute_test.schedule(schedule) # user API

        execute_test.execute_now(device=devices, schedule=schedule)
        execute_test.schedule(schedule)





