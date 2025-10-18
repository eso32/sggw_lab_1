import csv
from consts import ASSETS_DIR
from timed_decorator import timed

class ETL:
    def __init__(self, input_file):
        self.input_file = input_file

    def read_lines(self):
        with open(self.input_file, "r") as f:
            for line in f:
                yield line

    def process_line(self, line):
        parsed = [x for x in line.strip().split(",")]
        numeric_values = [float(x) for x in parsed[1:] if x != "-"]
        missing_values = [i+1 for i, x in enumerate(parsed[1:]) if x == "-"]
        total = sum(numeric_values)
        average = total / len(numeric_values) if numeric_values else 0
        return (parsed[0], total, average, missing_values)

    @timed
    def run_etl(self):

        missing_values_path  = ASSETS_DIR / 'missing_values.csv'
        values_path = ASSETS_DIR / 'values.csv'

        with open(missing_values_path, 'w') as missing_v_f, \
             open(values_path, 'w') as values_f:
                values_writer = csv.writer(values_f)
                missing_v_writer = csv.writer(missing_v_f)

                values_writer.writerow(['Order Number', 'Sum', 'Avg'])
                missing_v_writer.writerow(['Order Number', 'Missing values idices'])
                for line in self.read_lines():
                    i, total, average, missing_values = self.process_line(line)
                    values_writer.writerow([i, total, average])
                    missing_v_writer.writerow([i, missing_values])
        print(f'\nvalues -> {values_path}')
        print(f'missing values -> {missing_values_path} \n')