## How to run this program

1. Clone this repository to your local machine.
2. Navigate to the directory where the program files are located.
3. Open a terminal or command prompt.

### Using python

4. Run the tests using the following command:
    ```
    python .\test.py
    ```
5. You can also run the program individually by running the following command:
    ```
    python .\verify_json.py
    ```
    and inputting path to the file you desire do verify.

### Using Docker

4. Build the Docker image using the following command:
    ```
    docker build -t verify-json-app .
    ```
5. Run the Docker container using the following command:
    ```
    docker run verify-json-app
    ```

## How this program works and what it can return:

This program works by opening a file that (ideally) contains JSON that will have its Resource field analyzed if it contains a single asterisk.
Possible return values are:

1. `True`: The Resource field does not contain a single asterisk.
2. `False`: The Resource field contains a single asterisk.
3. `File not found`: The file specified could not be found.
4. `JSON parsing error: No Resource found`: The Resource field could not be found.
5. `JSON parsing error: No PolicyDocument or Statement found`: Either the PolicyDocument or Statement field could not be found.
6. `JSON decoding error`: There was an error while decoding JSON.