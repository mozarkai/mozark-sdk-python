# Getting Started

Every API call to MOZARK platform is authorized using an `api_access_token` created by a user as part of `login()` API. After you create a user account(or MOZARK provisions administrator account for you), you configure API URL, user credentials, and client ID in the config file as mentioned in the [SDK Configuration](#sdk-configuration) section below.

Table of contents
=================

* [Getting Started](#getting-started)
* [Table of contents](#table-of-contents)
  * [SDK Configuration](#sdk-configuration)
  * [User Authentication](#user-authentication)
    * [Login](#login)
    * [Logout](#logout)
  * [Project](#project)
    * [Create a project](#create-a-project)
    * [Get project information](#get-project-information)
    * [Delete a project](#delete-a-project)
    * [Get list of all projects](#get-list-of-all-projects)
  * [Application Builds](#application-builds)
    * [Upload an application package](#upload-an-application-package)
    * [Get application package information](#get-application-package-information)
    * [Delete application](#delete-application)
    * [Get list of all applications](#get-list-of-all-applications)
  * [Test Application Builds](#test-application-builds)
    * [Upload a native test application package](#upload-a-native-test-application-package)
    * [Get test application package information](#get-test-application-package-information)
    * [Delete test application](#delete-test-application)
    * [Get list of all test applications](#get-list-of-all-test-applications)
  * [Devices](#devices)
    * [Get list of all devices](#get-list-of-all-devices)
    * [Add devices](#add-devices)
  * [Device Trays](#device-trays)
    * [Create a device tray](#create-a-device-tray)
    * [Get a device tray information](#get-a-device-tray-information)
    * [Update a device tray](#update-a-device-tray)
    * [Delete a device tray](#delete-a-device-tray)
    * [Get device tray list](#get-device-tray-list)
  * [Test Configuration and Test Parameters](#test-configuration-and-test-parameters)
    * [Get supported test configuration](#get-supported-test-configuration)
    * [List of Test Parameters](#list-of-test-parameters)
  * [Executing a test](#executing-a-test)
    * [Execute a test now](#execute-a-test-now)
    * [Get test execution information](#get-test-execution-information)
    * [Abort test execution](#abort-test-execution)
    * [Get list of test runs](#get-list-of-test-runs)
  * [Scheduling tests](#scheduling-tests)
    * [Scheduling recurrent tests](#scheduling-recurrent-tests)
    * [Get test schedule information](#get-test-schedule-information)
    * [Delete test schedule](#delete-test-schedule)
    * [Get list of test schedules](#get-list-of-test-schedules)
    * [Update all tests in schedules](#update-all-tests-in-schedule)
    * [Update single test in schedules](#update-single-test-in-schedule)
  * [Analysing test outcomes](#analysing-test-outcomes)
    * [Get a complete test execution information](#get-a-complete-test-execution-information)
      * [Basic test information](#basic-test-information)
      * [Test Cases](#test-cases)
      * [User experience KPIs](#user-experience-kpis)
      * [Events](#events)
    * [Get test execution list](#get-test-execution-list)
    * [Get test execution information by information section](#get-test-execution-information-by-information-section)
      * [File URL](#file-url)
    * [Download test analytics information](#download-test-analytics-information)

## SDK Configuration

Configure API URL, user credentials, and client ID.

Create a configuration file with a name `config` under `.mozark` directory within your home folder. The template of the configuration file is as below:

```
[default]
MOZARK_APP_TESTING_URL={url}
MOZARK_APP_TESTING_USERNAME={username}
MOZARK_APP_TESTING_PASSWORD={password}
MOZARK_APP_TESTING_CLIENTID={client_id}
BASE_DOWNLOAD_DIR={local_download_base_dir}
```

## User Authentication

The `login()` api reads the information mentioned in `$HOME/.mozark/config` and sets the `api_access_token` to be further used in subsequent APIs.

### Login

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
```

### Logout

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.logout()
```

## Project

User can organize the application files, test application/code files, test executions, test outcomes etc. within a project. 

### Create a project

In order to create a project user should pass a unique project name along with an optional project description.

| Property            | Description                              |
|---------------------|------------------------------------------|
| project_name        | Unique project name(*mandatory*)         |
| project_description | A short note about a project(*optional*) |

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

project_name = "Android App Performance Testing"
project_description = "This project evaluate the quality of application experience in real user scenarios"

project_list = client.create_project(project_name=project_name, project_description=project_description)
```

### Get project information

To get project information of already created project, 

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

project_name = "Android App Performance Testing"
project_description = "This project evaluate the quality of application experience in real user scenarios"

project_info = client.get_project_info(project_name=project_name)

project_name = project_info["projectName"]
project_id = project_info["projectUUID"]
```

`get_project_info()` returns unique project identifier `projectUUID`

### Delete a project

```python
from mozark_sdk.client import Client

client = Client()

client.login()

project_name = "Android App Performance Testing"

response = client.get_project_info(project_name=project_name)
```

### Get list of all projects

Returns a list of all projects.

```python
from mozark_sdk.client import Client

client = Client()

client.login()

project_name = "Android App Performance Testing"

project_list = client.get_project_list()
```

## Application Builds

### Upload an application package

Upload android or ios application(.apk or .ipa) from given file path. 

| Property      | Description                                 |
|---------------|---------------------------------------------|
| file_category | File category (*mandatory*)                 |
| project_name  | Unique project name(*mandatory*)            |
| file_path     | Relative or absolute file path(*mandatory*) |

List of supported values for a `file_catogory`

* `android-application` -> For an android application package
* `ios-application` -> For an ios application package

`upload_application()` returns:

| Message                                          | Description |
|--------------------------------------------------|-------------|
| Success: File `file_name` uploaded successfully. | Success     |
| Failure: File `file_name` not uploaded.          | Failure     |
| Error: File `"file_name` already exists.         | Failure     |

---
**NOTE**

In order to avoid duplicate file uploads, MOZARK compares the md5 sum of already uploaded file with the file being uploaded now. Additionally, MOZARK uses file name to uniquely identify files, which can be referred by the user.

---

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

project_name = "Android App Performance Testing"
file_path = "./MyApplication-1.0.apk"
file_category = 'android-application'

message = client.upload_application(file_category=file_category,
                                    project_name=project_name,
                                    file_path=file_path)
```

### Get application package information

User can get information about the application file uploaded by passing the `file_name`.

`get_application_info()` returns a file information dictionary.

| Property     | Description                                            |
|--------------|--------------------------------------------------------|
| fileName     | Name of the file                                       |
| fileCategory | `android-application` or `ios-application`             |
| md5          | md5 checksum of a file                                 |
| fileURL      | http url of a file                                     |
| fileUUID     | unique identifier                                      |
| packageName  | Android package name(*for `android-application` only*) | 

`get_application_info()` returns an error message if file with a given file name is not found.

| Message                                        | Description |
|------------------------------------------------|-------------|
| Failure: File with name `file_name` not found. | Failure     |

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

file_name = "MyApplication-1.0.apk"

message = client.get_application_info(file_name=file_name)
```

### Delete application

User can delete the application file uploaded by passing the `file_name`.

`delete_application()` returns:

| Message                                         | Description |
|-------------------------------------------------|-------------|
| Success: File `file_name` deleted successfully. | Success     |
| Failure: File `file_name` not deleted.          | Failure     |

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

file_name = "MyApplication-1.0.apk"

message = client.delete_application(file_name=file_name)
```

### Get list of all applications

To get list of all application by giving a file category and an optional project name.

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

file_category = "android-application"
project_name = "Android App Performance Testing"

application_file_info_list = client.get_application_list(file_category=file_category,
                                                         project_name=project_name)
```

`get_application_list()` returns list of application info similar to `get_application_info()` as described in [Application File Info](#get-application-package-information)

## Test Application Builds

### Upload a native test application package

Upload native android or ios test application(.apk or .ipa) from given file path. 

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

project_name = "Android App Performance Testing"
file_path = "./my-experience-test-1.0.apk"
file_category = 'android-test-application'

message = client.upload_native_test_application(file_category=file_category,
                                                project_name=project_name,
                                                file_path=file_path)
```

`upload_native_test_application()` takes input parameter and returns the message same as mentioned in [Upload an application package](#upload-an-application-package)

List of supported values for a `file_catogory`

* `android-test-application` - For an android application package
* `ios-test-application` - For an ios application package

### Get test application package information

User can get information about the application file uploaded by passing the `file_name`.

`get_native_test_application_info()` returns a file information dictionary as described in [Get Application Package Information](#get-application-package-information).

In addition to the common properties, `get_native_test_application_info()` also returns following information which is specific to the native test application. MOZARK derives these values by processing the uploaded .apk and .ipa files. 

These properties are essential for running the test successfully, user must ensure the correctness of these values as per the information specified in their android or ios test code projects.

| Property            | Description                                                                        |
|---------------------|------------------------------------------------------------------------------------|
| testCodePackageName | Package name specified in the test code, present in `android-test-applcation` only |
| testRunnerName      | Runner name specified in the test code, present in `ios-test-applcation` only      |
| XCTestRunFileUrl    | XCTestRun file bundled with test code, present in `ios-test-applcation` only       |

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

file_name = "my-experience-test-1.0.apk"

message = client.get_native_test_application_info(file_name=file_name)
```

### Delete test application

User can delete the test application file uploaded by passing the `file_name`.

`delete_native_test_application()` works similar to `delete_application()` :

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

file_name = "my-experience-test-1.0.apk"

message = client.delete_native_test_application(file_name=file_name)
```

### Get list of all test applications

To get list of all test application by giving a file category and an optional project name.

`get_native_test_application_list()` works similar to the `get_application_list()`. 

The properties returned in the file info dictionary are same as described in [Get test application package information](#get-test-application-package-information)

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

file_category = "android-test-application"
project_name = "Android App Performance Testing"

test_application_file_info_list = client.get_native_test_application_list(file_category=file_category,
                                                                     project_name=project_name)
```

## Devices

### Get list of all devices

User can get list of real devices provisioned by specifying the platform.

List of supported platforms:

| Platform    | Description                                            |
|-------------|--------------------------------------------------------|
| android     | Devices installed with Android OS                      |
| ios         | Devices installed with iOS                             |
| living-room | Living room devices like TVs, which has its own OS.    |

`get_device_list()` returns a list of device information json objects. The properties of this object are described below:

| Property          | Description                                         |
|-------------------|-----------------------------------------------------|
| deviceSerial      | Unique identifier provided by a device manufacturer |
| deviceBrand       | Brand name of the device                            |
| deviceCity        | City in which device is located                     |
| deviceCountry     | Country in which device is located                  |
| deviceModelName   | Model name of the device                            |
| deviceModelNumber | Model number of the device                          |
| devicePlatform    | `android` or `ios` or `living-room`                 |
| deviceOSVersion   | OS version installed on the device                  |
| deviceSDKVersion  | List of supported SDK versions by device OS         |
| deviceUUID        | Unique identifier of the device(MOZARK)             |
| deviceNetwork     | Network to which the device is connected to         |

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

device_list = client.get_device_list(platform='android')
```


### Add devices

User can add devices in platform.

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
device_parameter = {
              "brand": "Samsung",
              "modelName": "Galaxy M20",
              "serial": "3401868eba0a16fd",
              "platform": "android",
              "osVersion": "8.1.0",
              "modelNumber": "",
              "sdkVersion": [
                "31",
                "32"
              ],
              "deviceParameters": {
                "controllerId": "dubai-mac-1",
                "city": "Dubai",
                "country": "United Arab Emirates",
                "network": "",
                "liveLog": "https://{TenantName}}-logs.mozark.ai:10024",
                "deviceStatus": "free",
                "appiumPort": "4933",
                "mjpegServerPort": "1047",
                "systemPort": "8224",
                "chromedriverPort": "8024"
              },
              "logParameters": {
                "serverIpAddress": "{TenantName}}-logs.mozark.ai",
                "serverUserName": "ubuntu",
                "port": "10024",
                "mitmPort": "8024"
              }
            }

response = client.add_device(device_parameter=device_parameter)
```


---
**NOTE**

In order to execute test on the device, MOZARK APIs only need list of `deviceSerial` other properties are useful to pick and choose devices from provisioned list.

---

## Device Trays

Device trays is useful feature to allow user to save the list of devices for future use.

### Create a device tray

User can create a device tray by passing platform, unique tray name, and a list of device serial numbers.

List of supported platforms is same as described in a [Get list of all devices](#get-list-of-all-devices).

User can construct the list of device serial numbers from the output of  `get_device_list()`.

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

tray_name = "Android 10 Devices in Mumbai"

device_list = ["a1234a", "a1234b", "a1234c"] # use get_device_list() to construct this

message = client.create_tray(platform='android',
                             tray_name=tray_name,
                             device_list=device_list)
```

### Get a device tray information

User can get tray information for a given tray name.

`get_tray_info()` returns json object with a tray name, platform name, along with list of devices added in the tray.

`get_tray_info()` returns a list of devices under `trayDevices` key. The information of the devices is same as described in [Get list of all devices](#get-list-of-all-devices)

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

tray_name = "Android 10 Devices in Mumbai"

tray_info = client.get_tray_info(tray_name=tray_name)
```

### Update a device tray

User can update the list of devices in a given tray. `update_tray()` replaces the existing list of devices with a newly passed device list.

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

tray_name = "Android 10 Devices in Mumbai"

updated_device_list = ["a1234x", "a1234y", "a1234z"] # use get_device_list() to construct this

message = client.update_tray(tray_name=tray_name,
                             device_list=updated_device_list)
```

### Delete a device tray

User can delete a tray by passing a tray name.

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

tray_name = "Android 10 Devices in Mumbai"

message = client.delete_tray(tray_name=tray_name)
```

### Get device tray list

User can get a list of device trays. 

`get_tray_list()` returns a list of objects containing tray name, tray platform, and tray id.

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

tray_list = client.get_tray_list()
```

## Test Configuration and Test Parameters

MOZARK enables various features to capture information while executing the application user scenario. The access to these features is made flexible by a test configuration and test parameters.

List of supported test configuration and how to set up test parameters is described in below sections.

### Get supported test configuration

List of supported test configurations:

| Feature                                                                                                 | Key                            | Platform     |
|---------------------------------------------------------------------------------------------------------|--------------------------------|--------------|
| Capture and store test code/application console logs                                                    | captureAutomationLogs          | all          |
| Capture and store test framework output files                                                           | captureTestFrameworkResult(*)  | all          |
| Capture and store device logs while user scenarios is being run                                         | captureSystemDebugLogs         | all          |
| Capture and store device screenshots while user scenario is being run                                   | captureDeviceScreenShots       | all          |
| Record and store device screen as a video while user scenario is being run                              | recordDeviceScreen             | android, ios |
| Capture and store HTTP APIs request and response between application and its backend                    | captureHAR                     | android      |
| Capture and store Device TCP traffic between application and its backend                                | captureDeviceNetworkPackets(*) | none         |
| Capture and store CPU metrics while user scenario is being run                                          | captureCPUMetrics(*)           | android, ios |
| Capture and store Memory metrics while user scenario is being run                                       | captureMemoryMetrics(*)        | android, ios |
| Capture and store Battery metrics while user scenario is being run                                      | captureBatteryMetrics(*)       | android      |
| Capture and store Graphics metrics while user scenario is being run                                     | captureGraphicsMetrics(*)      | android      |
| Record and store TV screen as a video while user scenario is being run on device                        | recordLRDeviceScreen(*)        | living-room  |
| Start live streaming of test code/application console logs while user scenario is being run on device   | captureLiveLogs                | all          |

---
**NOTE**

For the key marked with (*) and its respective feature is supported from SDK, but the platform support communicated as part of feature release.

---

The default value to all the above feature keys is set to `false`. User can set desired test configuration properties to `true` and pass it while [Executing a test](#execute-a-test-now) or [Scheduling tests](#scheduling-recurrent-tests).

*Example*:

```python
test_configuration = {
  "captureHAR": True,
  "captureDeviceScreenShots": True,
  "recordDeviceScreen": True,
  "captureSystemDebugLogs": True,
  "captureLiveLogs": True
}
```

### List of Test Parameters

## Executing a test

### Execute a test now

To execute test on set of devices, User need to pass following parameters to `start_test_execution()` API.

| Parameter                  | Description                                                                                              |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| project_name               | Name of the project                                                                                      |
| test_framework             | Application automation testing framework                                                                 |
| application_file_name      | Name of application package file uploaded                                                                |
| test_application_file_name | Name of test application package file uploaded                                                           |
| devices                    | List of device serials                                                                                   |
| test_configuration         | Test configuration see [Test Configuration and Test Parameters](#test-configuration-and-test-parameters) |
| test_parameters            | Test parameters see [Test Configuration and Test Parameters](#test-configuration-and-test-parameters)    |

List of supported test frameworks:

* `android-uiautomator` - Android native test framework
* `ios-xcuitest` - iOS native test framework
* `lr-android-uiautomator` - Living room device automation uses Android native test framework to automate TV remote control app.

`start_test_execution()` returns a success message `Success: Executed/Scheduled successfully` along with the `testId` if the execution request is submitted successfully.

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

tray_list = client.get_tray_list()
project_name = "Android App Performance Testing"
test_framework = "android-uiautomator"
application_file_name = "MyApplication-1.0.apk"
test_application_file_name = "my-experience-test-1.0.apk"
devices = ["a1234a", "a1234b", "a1234c"]
test_configuration = {
  "captureHAR": True,
  "captureDeviceScreenShots": True,
  "recordDeviceScreen": True,
  "captureSystemDebugLogs": True,
  "captureLiveLogs": True
}
test_parameters = {
  "maxTestDuration": 10
}
response = client.start_test_execution(project_name=project_name,
                                       test_framework="android-uiautomator",
                                       application_file_name=application_file_name,
                                       test_application_file_name=test_application_file_name,
                                       devices=devices,
                                       test_configuration=test_configuration,
                                       test_parameters=test_parameters
                                       )
```

### Get test execution information

After the test execution request is submitted, user can monitor the test status by checking the test information.

In addition to the parameters passed to `start_test_execution()`, `get_test_info()` returns following information:

| Key                   | Description                                               |
|-----------------------|-----------------------------------------------------------|
| testStartTime         | Date and time when the test execution is actually started |
| testEndTime           | Date and time when the test execution is test completed   |
| testUUID              | Unique ID of the test                                     |
| testStatus            | Status of the test                                        |
| testStatusDescription | Sub-status or Error description of a test status          |

List of test status and its description:

| Test Status | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| SCHEDULED   | Test execution request is submitted but test run is not yet started         |
| STARTED     | Test run has started                                                        |
| COMPLETED   | Test run has completed                                                      |
| ABORTED     | Test run is aborted before it has finished `maxTestDuration`                |
| FAILED(*)   | Test run has completed, but all the test cases in the test suite has failed |

---
**NOTE**

TODO: Include `FAILED` test status

---

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
test_id = "aa1234bb" # testUUID 
test_info = client.get_test_info(test_id=test_id)
```

### Abort test execution

User can abort test execution of a test which is running at the time of abort. 

```python
from mozark_sdk.client import Client

client = Client()

client.login()
test_id = "aa1234bb" # testUUID 
test_info = client.abort_test_execution(test_id=test_id)
```

### Get list of test runs

User can get list of test runs. `get_test_list()` returns list of test information objects as described in [Get test execution information](#get-test-execution-information).

---
**NOTE**

Filter options `from_date_time` and `to_date_time` will be implemented in next release.

---

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
test_id = "aa1234bb" # testUUID 
test_info = client.get_test_list()
```

## Scheduling tests

Scheduling tests to execute in a recurrent manner could be useful in various scenarios. These scenarios may include but not limited to following:

* Evaluate user experience by running same user scenarios throughout day or at specific time on a day.
* Collect multiple test outcome - app performance metrics, user experience metrics etc. - to make data driven decision for product development.
* Multiple test runs planned within schedule can be deleted easily.

### Scheduling recurrent tests

Scheduling recurrent tests is similar to executing test now. In addition to the parameters passed in `start_test_execution()` (see [Execute a test now](#execute-a-test-now)), following parameters are required.

| Parameter       | Description                                                           |
|-----------------|-----------------------------------------------------------------------|
| start_date_time | Date and time when schedule will start                                |
| end_date_time   | Date and time when schedule will end                                  |
| interval        | Interval(*in minutes*) between two test runs in a scheduled execution |

`interval` should be greater than `maxTestDuration` in `test_parameters`. 

`schedule_test_execution()` returns a status message along with `scheduleUUID` and list of test runs after the schedule test execution request is submitted successfully. 

* `testStartDateTime` mentioned in a test object within `testRuns` array denote actual test start time when the test run is picked up for execution or the test run has completed execution. Alternatively, it denotes expected test start date and time if the test is yet to run(or the date time is in future).

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()

tray_list = client.get_tray_list()
project_name = "Android App Performance Testing"
test_framework = "android-uiautomator"
application_file_name = "MyApplication-1.0.apk"
test_application_file_name = "my-experience-test-1.0.apk"
devices = ["a1234a", "a1234b", "a1234c"]
test_configuration = {
  "captureHAR": True,
  "captureDeviceScreenShots": True,
  "recordDeviceScreen": True,
  "captureSystemDebugLogs": True,
  "captureLiveLogs": True
}
test_parameters = {
  "maxTestDuration": 10
}

schedule_start_date_time = "2023-01-03T22:00:00.000+05:30"
schedule_end_date_time = "2023-01-05T23:00:00.000+05:30"

interval = 15

response = client.schedule_test_execution(project_name=project_name, 
                                          test_framework="android-uiautomator",
                                          application_file_name=application_file_name,
                                          test_application_file_name=test_application_file_name,
                                          devices=devices,
                                          test_configuration=test_configuration,
                                          test_parameters=test_parameters,
                                          start_date_time=schedule_start_date_time,
                                          end_date_time=schedule_end_date_time,
                                          interval=interval)
```

Submitting request for scheduling test runs will fail if the device slots in existing schedules conflicts with the new request. Getting a schedule information could help choose the free device slots for new schedule.

### Get test schedule information

User can get test execution schedule information by passing `schedule_id` to `get_test_schedule_info()`. This API returns common parameters used while scheduling the test execution and a test specific parameters as specified below:

Schedule information:

```json
{
  "scheduleUUID": "",
  "scheduleStartTime": "",
  "scheduleEndTime": "",
  "testInterval": "",
  "testConfiguration": {},
  "testParameters": {},
  "projectName" : "",
  "testFramework": "android-uiautomator | ios-xcuitest | living-room-automate",
  "applicationFileName": "",
  "testApplicationFileName": ""
}
```

Test specific information
```json
{
    "device": "",
    "testStartTime": "",
    "testEndTime": "",
    "testUUID": "",
    "testStatus": "SCHEDULED | STARTED | COMPLETED | ABORTED | FAILED",
    "testStatusDescription": ""
}
```

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
schedule_id = "aa1234bb" # scheduleUUID 
schedule_info = client.get_test_schedule_info(schedule_id=schedule_id)
```


### Delete test schedule

User can delete a test schedule by passing a `schedule_id` passed in `delete_test_schedule()`.

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
schedule_id = "aa1234bb" # scheduleUUID 
response = client.delete_test_schedule(schedule_id=schedule_id)
```

Deleting a test execution schedule deletes all the test runs which are yet to start execution at the time of schedule deletion.

### Get list of test schedules

User can get list of all schedules, the `get_test_schedule_list()` returns list of schedule information same as described in [Get test schedule information](#get-test-schedule-information).

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
schedule_info = client.get_test_schedule_list()
```


### Update all tests in schedule

User can test parameter in all test present in schedule by passing a `schedule_id` and `update_data` passed in `update_schedule()`.

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
schedule_id = "f0abd6ea-83db-46ca-99b3-d5bcb6931d6c" # scheduleUUID
update_data = {
            "testParameters": {
                "packageName": "some name",
                "custom key": "custom value"
            }
        }
response = client.update_schedule(data=update_data,schedule_id=schedule_id)
```

### Update single test in schedule

User can update test parameter in a single test by passing a `test_id` and `update_data` passed in `update_test()`.

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
test_id = "a1c2e491-78be-47a1-aed8-7ca242b6a579" # testUUID
update_data = {
            "testParameters": {
                "packageName": "some name",
                "custom key": "custom value"
            }
        }
response = client.update_test(data=update_data,test_id=test_id)
```

---
**NOTE**

Filter options `from_date_time` and `to_date_time` will be implemented in next release.

---

## Analysing test outcomes

### Get a complete test execution information

Based on the test configuration, test outcome has various sections to display useful information about a test run.

#### Basic test information

Basic information about the test run includes:

| Key                     | Description                                                      |
|-------------------------|------------------------------------------------------------------|
| testUUID                | Unique test ID                                                   |
| testStartDateTime       | Start date time of a test run                                    |
| testEndDateTime         | Date time when the test run was completed                        |
| projectName             | Project name                                                     |
| applicationFileName     | Uploaded application file name                                   |
| testApplicationFileName | Uploaded test application file name                              |
| deviceSerial            | Device serial                                                    |
| deviceMake              | Make of a device                                                 |
| deviceModel             | Model of a device                                                |
| deviceCity              | City where device is provisioned                                 |
| deviceCountry           | Country in which device is provisioned                           |
| deviceNetwork           | Network which is enabled during test execution                   |
| devicePlatform          | `android`, `ios`, or `living-room`                               |
| deviceOSVersion         | Version of OS installed in a device                              |
| deviceNetworkOperator   | Name of a network operator chosen while executing a test         |
| testStatus              | `SCHEDULED` or `STARTED` or `COMPLETED` or `ABORTED` or `FAILED` |
| testStatusDescription   | Test status description                                          |
| testCasesTotal          | Total number of test cases executed                              |
| testCasesPassed         | Total number of test cases passed                                |
| testCasesFailed         | Total number of test cases failed                                |

#### Test Cases

| Key                      | Description                                                 |
|--------------------------|-------------------------------------------------------------|
| testCaseName             | test case name                                              |
| testCaseResult           | `PASS` or `FAIL`                                            |
| testCaseStartDateTime(*) | Date and time when the test code flow entered the test case |
| testCaseEndDateTime(*)   | Date and time when the test code flow exited the test case  |

---
**NOTE**

`testCaseStartDateTime` and `testCaseEndDateTime` can be captured if the test framework support.

---

#### User experience KPIs

User experience KPIs are derived from the events captured during the automated user journey from the test code. These are captured within a scope of a test case. 

`userExperienceKpis` section list all the KPIs which can be calculated based on events captured within a test case.

| Key          | Description                                                 |
|--------------|-------------------------------------------------------------|
| kpiName      | Name of the KPI                                             |
| kpiValue     | Value of KPI                                                |
| testCaseName | Test case name within the events for this KPI were captured |

(see [How KPIs are calculated](./documentation/user-experience-kpis.md#how-kpis-are-calculated)

#### Events 

User can capture and send events during the user journey within test code. These events are further used to send notification or calculate user experience KPIs.

(see [How to capture events from the test code](./documentation/user-experience-kpis.md#how-to-capture-events-from-the-test-code))

This section lists all the events captured during the test run. It includes:

| Key           | Description                                  |
|---------------|----------------------------------------------|
| eventName     | Name of the event                            |
| eventDateTime | Date and time at which the event is captured |
| testCaseName  | Test case name within this event is captured |

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
test_id = "aa1234bb" # testUUID 
response = client.get_test_execution_info_full(test_id=test_id)
```
### Get test execution list

User can get list of all test execution information by passing `from_date_time` and `to_date_time` to get_test_list(). This API returns list of test information same as described in [Execute a test now](#execute-a-test-now).

*Example*:

```python
from mozark_sdk.client import Client
import datetime

client = Client()

client.login()
from_date_time = datetime(2023, 1, 7, 0, 0, 0)
to_date_time = datetime(2023, 1, 8, 0, 0, 0)
test_info_list = client.get_test_list(from_date_time=from_date_time,to_date_time=to_date_time)
```

### Get test execution information by information section

| Section name                            | Description                                               | Response/File Type         |
|-----------------------------------------|-----------------------------------------------------------|----------------------------|
| basic_test_info                         | same as [Basic test information](#basic-test-information) | json                       |
| test_configuration                      | Same as [Test configuration](#test-configuration)         | json                       |
| test_cases                              | Same as [Test cases](#test-cases)                         | json                       |
| events                                  | Same as [Events](#events)                                 | json                       |
| kpis_user_experience                    | Same as [User experience KPIs](#user-experience-kpis)     | json                       |
| kpis_api_performance_http               | Same as [User experience KPIs](#user-experience-kpis)     | json                       |
| files_device_screenshots                | List of File URLs - same as [File URL](#file-url)         | png                        |
| files_device_screen_record              | Same as [File URL](#file-url)                             | mp4                        |
| files_har                               | Same as [File URL](#file-url)                             | har                        |
| files_device_cpu_metrics                | Same as [File URL](#file-url)                             | csv                        |
| files_device_memory_metrics             | Same as [File URL](#file-url)                             | csv                        |
| files_device_battery_metrics            | Same as [File URL](#file-url)                             | csv                        |
| files_device_graphics_metrics           | Same as [File URL](#file-url)                             | csv                        |
| files_device_network_packets            | Same as [File URL](#file-url)                             | pcap                       |
| files_device_debug_logs                 | Same as [File URL](#file-url)                             | log                        |
| files_test_execution_output             | Same as [File URL](#file-url)                             | log                        |
| files_test_framework_output             | Same as [File URL](#file-url)                             | log or xml or json or html |
| kpis_system_performance_cpu_metrics     | Same as [User experience KPIs](#user-experience-kpis)     | json                       |
| kpis_system_performance_memory_metrics  | Same as [User experience KPIs](#user-experience-kpis)     | json                       |
| kpis_system_performance_battery_metrics | Same as [User experience KPIs](#user-experience-kpis)     | json                       |
| kpis_app_performance_graphics_metrics   | Same as [User experience KPIs](#user-experience-kpis)     | json                       |

#### File URL

Structure is as below:

```json
{
  "fileURL" : ""
}
```
*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
test_id = "aa1234bb" # testUUID 
section = "basic_test_info"
response = client.get_test_execution_info_by_section(test_id=test_id,section=section)
```
### Download test analytics information

User can download test analytics information for various sections in the format specified in [Section information](#get-test-execution-information-by-information-section)

*Example*:

```python
from mozark_sdk.client import Client

client = Client()

client.login()
test_id = "aa1234bb" # testUUID 
section = "basic_test_info"
response = client.download_by_section(test_id=test_id,section=section)
```