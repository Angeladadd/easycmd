import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

class Storage:

    def __init__(self, file_storage_path):
        self._file_storage_path = file_storage_path
        self._alias_2_command = {}
        self.__read_csv_to_map()
        self._commands = list(self._alias_2_command.keys())

    def cache(self, command, alias=None):
        if not alias:
            alias = command
        rows = []
        if not alias in self._alias_2_command:
            rows.append([alias, command])
        if alias != command and not command in self._alias_2_command:
            rows.append([command, command])
        self.__append_to_csv(rows)
        
    def match(self, input):
        matches = process.extract(input, self._commands, scorer=fuzz.partial_ratio)
        matched_values = [match[0] for match in sorted(matches, key=lambda m: m[1], reverse=True)]
        alias = matched_values[:min(10, len(matched_values))]
        return {a: self._alias_2_command[a] for a in alias}
    
    def __append_to_csv(self, rows):
        if len(rows) == 0:
            return
        with open(self._file_storage_path, 'a', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                writer.writerow(row)
    
    def __read_csv_to_map(self):
        with open(self._file_storage_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                key = row[0]
                values = row[1:][0]
                self._alias_2_command[key] = values