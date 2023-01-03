# Getting Started

Every API call to MOZARK platform is authorized using an `api_access_token` created by a user as part of `login()` API. After you create a user account(or MOZARK provisions administrator account for you), you configure API URL, user credentials, and client ID in the config file as mentioned in the [SDK Configuration](#sdk-configuration) section below.

Table of contents
=================
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
* [Analysing test outcomes](#analysing-test-outcomes)
  * [Get test execution information](#get-test-execution-information-1)
  * [Get test execution information by information section](#get-test-execution-information-by-information-section)
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
project_description = project_info["projectDescription"]
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

### Get test execution information

### Abort test execution

### Get list of test runs

## Scheduling tests

### Scheduling recurrent tests

### Get test schedule information

### Delete test schedule

### Get list of test schedules

## Analysing test outcomes

### Get test execution information

### Get test execution information by information section

### Download test analytics information




