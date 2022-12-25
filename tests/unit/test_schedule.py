from unittest import TestCase

class TestSchedule(TestCase):
    def test_schedule_initialize(self):
        start_time = None
        devices = ["abc", "xyz"]
        test_configuration = {"captureCPUMetrics": True, "captureLiveLogs" : True}
        test_configuration.CAPTURE_CPU_METRICS = True


