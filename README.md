
## Mozark-SDK usage :-

### Get started :-
- Create a .mozark directory under HOME folder
- Create a config file under .mozark directory
- Sample file contents inside config file
    ```commandline
    [default]
    MOZARK_APP_TESTING_URL=MOZARK_URL
    MOZARK_APP_TESTING_USERNAME=MOZARK_USER_NAME
    MOZARK_APP_TESTING_PASSWORD=MOZARK_USER_PASSWORD
    MOZARK_APP_TESTING_CLIENTID=MOZARK_CLIENT_ID
    ```
- Get you MOZARK credentials from mozark portal and replace the values

### Client Usage :-
- Import Client
  ```commandline
    from mozark_sdk.client import Client
  ```
- Create a client object
  ```commandline
    client = Client()
  ```
- Login to use other functionalities
  ```commandline
    clinet.login()
  ```