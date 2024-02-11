import json

class PersistentDict:
    """Basic class for persistint a record of data about article sentiment
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, 'r') as json_file:
                data = json.load(json_file)
            return data
        except FileNotFoundError:
            return {}

    def save(self):
        with open(self.file_path, 'w') as json_file:
            json.dump(self.data, json_file, indent=2)

    def get_numbers(self, name):
        return self.data.get(name, (None, None))

    def set_numbers(self, name, number1, number2):
        self.data[name] = (number1, number2)
        self.save()

    def delete_name(self, name):
        if name in self.data:
            del self.data[name]
            self.save()