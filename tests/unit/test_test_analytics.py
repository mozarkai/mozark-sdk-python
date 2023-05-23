from mozark_sdk.client import Client
from unittest import TestCase
from datetime import datetime


class TestTestAnalytics(TestCase):

    def test_get_test_list(self):
        client = Client()
        client.login()
        # from_date_time = datetime(2023, 1, 3, 18, 0, 0, tzinfo=ZoneInfo('Asia/Kolkata'))
        # to_date_time = datetime(2023, 1, 3, 19, 0, 0, tzinfo=ZoneInfo('Asia/Kolkata'))
        from_date_time = datetime(2023, 1, 3, 0, 0, 0)
        to_date_time = datetime(2023, 1, 3, 0, 0, 0)
        response = client.get_test_list(from_date_time=from_date_time, to_date_time=to_date_time)
        print("\n 1 get test list : ", response)

    def test_get_test_execution_info_full(self):
        client = Client()
        client.login()
        # test_id = '5a1126d2-9927-43fc-acda-61255b45ad3b'
        test_id = '95549b4f-24a0-4a9e-8520-2fbcf7db0f12'
        response = client.get_test_execution_info_full(test_id=test_id)
        print("\n 2 get test information : ", response)

    def test_get_test_execution_info_by_section(self):
        client = Client()
        client.login()
        test_id = '95549b4f-24a0-4a9e-8520-2fbcf7db0f12'
        # section = 'basic_test_info'
        # section = 'test_configuration'
        # section = 'test_cases'
        # section = 'events'
        # section = 'kpis_user_experience'
        # section = 'kpis_api_performance_http'
        # section = 'files_device_screenshots'
        section = 'files_device_screen_record'
        section = 'files_har'
        # section = 'files_device_cpu_metrics'
        # section = 'files_device_memory_metrics'
        # section = 'files_device_battery_metrics'
        # section = 'files_device_graphics_metrics'
        # section = 'files_device_network_packets'
        # section = 'files_device_debug_logs'
        # section = 'files_test_execution_output'
        # section = 'files_test_framework_output'
        # section = 'kpis_system_performance_cpu_metrics'
        # section = 'kpis_system_performance_memory_metrics'
        # section = 'kpis_system_performance_battery_metrics'
        # section = 'kpis_app_performance_graphics_metrics'
        response = client.get_test_execution_info_by_section(test_id=test_id, section=section)
        print("\n 3 get test information by section: ", response)

    def test_download_by_section(self):
        client = Client()
        client.login()
        test_id = '95549b4f-24a0-4a9e-8520-2fbcf7db0f12'
        # section = 'basic_test_info'
        # section = 'test_configuration'
        # section = 'test_cases'
        # section = 'events'
        # section = 'kpis_user_experience'
        # section = 'kpis_api_performance_http'
        section = 'files_device_screenshots'
        # section = 'files_device_screen_record'
        # section = 'files_har'
        # section = 'files_device_cpu_metrics'
        # section = 'files_device_memory_metrics'
        # section = 'files_device_battery_metrics'
        # section = 'files_device_graphics_metrics'
        # section = 'files_device_network_packets'
        # section = 'files_device_debug_logs'
        # section = 'files_test_execution_output'
        # section = 'files_test_framework_output'
        # section = 'kpis_system_performance_cpu_metrics'
        # section = 'kpis_system_performance_memory_metrics'
        # section = 'kpis_system_performance_battery_metrics'
        # section = 'kpis_app_performance_graphics_metrics'
        # file_name = 'battery.txt'
        # section = 'screenshots'
        # file_name = '2023-01-02T23-40-26-305650.jpg'
        response = client.download_by_section(test_id=test_id, section=section)
        print("\n 4 get test information : ", response)
