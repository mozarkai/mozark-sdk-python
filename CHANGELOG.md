# CHANGELOG

## 0.5 - 2023-01-03

### User 
* [ADDED] Login for obtaining authentication-toke to use other functionalities
* [ADDED] Logout for closing an authenticated session

### Project
* [ADDED] `create_project` for creating a project
* [ADDED] `get_project_info` for getting project information
* [ADDED] `delete_project` for deleting project
* [ADDED] `get_project_list` for listing all projects

### File
* [ADDED] `get_application_info` for getting file information
* [ADDED] `delete_application` for deleting application
* [ADDED] `get_application_list` for listing all application file information
* [ADDED] `upload_native_test_application` for uploading native test application
* [ADDED] `get_native_test_application_info` for getting native test application information
* [ADDED] `delete_native_test_application` for deleting native test application
* [ADDED] `get_native_test_application_list` for listing all native application

### Devices
* [ADDED] `get_device_list` for listing device information of all devices
* [ADDED] `add_device` for adding devices in portal

### Tray
* [ADDED] `create_tray` for creating tray
* [ADDED] `get_tray_info` for getting information of tray
* [ADDED] `update_tray` for updating device list in a tray
* [ADDED] `delete_tray` for deleting tray
* [ADDED] `get_tray_list` for listing all the trays created

### Execution
* [ADDED] `start_test_execution` for testing now
* [ADDED] `get_test_info` for getting information of a test run
* [ADDED] `abort_test_execution` for aborting a test run
* [ADDED] `schedule_test_execution` for scheduling test
* [ADDED] `get_test_schedule_info` for getting information of a schedule
* [ADDED] `delete_test_schedule` for deleting scheduled tests
* [ADDED] `get_test_schedule_list` for listing all the schedules added
* [ADDED] `update_schedule` for update any test parameters in all test 
* [ADDED] `update_test` for update any test parameters in a single test.



### Analytics
* [ADDED] `get_test_list` for listing all the test runs
* [ADDED] `get_test_execution_info_full` for getting all information of a test run
* [ADDED] `get_test_execution_info_by_section` for getting a section information of a test run
* [ADDED] `download_by_section` for downloading test run information as a json file, raw file, list of raw files