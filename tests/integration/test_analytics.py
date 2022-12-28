import os
import logging
from mozark_sdk.client import Client
from unittest import TestCase


class TestStartTestExecution(TestCase):

    def test_analytics_functionalities(self):
        client = Client()
        # client.set_config()
        client.login()
        test_list = client.get_test_list()
        # print(test_list)
        test_id = test_list[0]['uuid']['testId']
        print(test_id)
        test_info = client.get_test_execution_info_full(test_id)
        print(test_info)
        screenshot_list = test_info['screenshots']
        log_list = test_info['logs']
        resp = client.download_test_screenshot(test_id, screenshot_list[0],
                                        '/Users/sumitkumargupta/.mozark/'+screenshot_list[0])
        print(resp)
        resp = client.download_test_screenshot(test_id, log_list[0],
                                        '/Users/sumitkumargupta/.mozark/' + log_list[0])
        print(resp)
        # resp = client.download_test_log(test_id, 'execution.log',
        #                                 '/Users/sumitkumargupta/.mozark/' + 'execution.log')
        # print(resp)


