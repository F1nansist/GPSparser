"""
Класс для парсинга форматов gps-лога.
По необходимости, можно добавить и другие форматы и тип наполнения и дописать в классе.
Все указанные в классе форматы с наполнение типов будут обработаны.
Была добавлена только обработка входного файла (можно еще и строку входную сделать для обработки в реальном времени).
Выходной тип есть только один (print), но можно также сделать в виде файла или архивирование в БД или еще где угодно.
"""


class GPSParser:
    gps_id_arr = ['GNRMC']
    gps_id = {'GNRMC': ('Id', 'UTC', 'Status', 'Latitude', 'NS', 'Longtitude', 'WE', 'Speed', 'Track angle',
                        'Date', 'Magnetic variation', 'Strange thing', 'WE', 'Checksum data')}

    def __init__(self, path_to_gps_data, output_type='print'):
        # path to data file
        self.path_to_data = path_to_gps_data
        # parsers output type
        # now is working only 'print' type which print chosen gps-format on the screen
        self.output_data = output_type

    # deleting trash symbols from string
    @staticmethod
    def delete_trash_symbols(line):
        trash_symbols = ('b', '\\', 'r', 'n', '\'', '$')
        for tr_symb in range(len(trash_symbols)):
            line = line.replace(trash_symbols[tr_symb], '')
        return line

    def start_parser(self):
        # reading file and saves data as string lines
        file = open(self.path_to_data, 'r')
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.strip()
            line = self.delete_trash_symbols(line)  # deleting trash symbols
            line = line.replace('*', ',')
            line_arr = line.split(',')  # making an array from each string

            # verifyoing if gps format in existed string is existing in class data for processing
            if line_arr[0] in self.gps_id_arr:
                iterations = len(self.gps_id.get(line_arr[0]))

                # output type of parser
                if self.output_data == 'print':
                    for i in range(iterations):
                        if line_arr[i] != '':
                            # printing output data for chosen gps format
                            print(f'{self.gps_id.get(line_arr[0])[i]}: {line_arr[i]}. ', end='')
                    print()
