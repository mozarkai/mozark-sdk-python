# Getting Started

Every API call to MOZARK platform is authorized using an `api_access_token` created by a user as part of `login()` API. After you create a user account(or MOZARK provisions administrator account for you), you configure API URL, user credentials, and client ID in the config file as mentioned in the [SDK Configuration](#sdk-configuration) section below.

Table of contents
=================

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
```python
from mozark_sdk.client import Client

client = Client()

client.login()
```

### Logout

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
- `android-application` -> For an android application package
- `ios-application` -> For an ios application package

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

```python
from mozark_sdk.client import Client

client = Client()

client.login()

file_name = "MyApplication-1.0.apk"

message = client.delete_application(file_name=file_name)
```

### Get list of all applications

To get list of all application by giving a file category and an optional project name.

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
- `android-test-application` -> For an android application package
- `ios-test-application` -> For an ios application package

### Get test application package information

### Delete test application

### Get list of all test applications

## Devices

### Get list of all devices

## Device Trays

### Create a device tray

### Get a device tray information

### Update a device tray

### Delete a device tray

### Get device tray list

## Test Configuration and Test Parameters

### Get supported test configuration

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




