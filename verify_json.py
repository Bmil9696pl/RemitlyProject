import json

class JSONParsingException(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)

def verifyJson(jsonFile):
    try:
        with open(jsonFile, 'r') as file:
            jsonData = json.load(file)
            statements = jsonData.get('PolicyDocument', {}).get('Statement', [])
            if statements:
                for statement in statements:
                    resource = statement.get('Resource')
                    if resource:
                        if resource == '*':
                            return False
                    else:
                        raise JSONParsingException("No Resource found")
            else:
                raise JSONParsingException("No PolicyDocument or Statement found")

    except FileNotFoundError:
        return "File not found"
    except json.JSONDecodeError as error:
        return f"JSON decoding error: {str(error)}"
    except JSONParsingException as error:
        return f"JSON parsing error: {str(error)}"
    
    return True

if __name__ == '__main__':
    filename = input("Input path to the tested file:\n")
    print(verifyJson(filename))