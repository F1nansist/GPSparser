from GPSParser import GPSParser

if __name__ == '__main__':

    # path to data file
    path_to_gps_data = 'gps_data.txt'

    # creating an object with required atributes and starts parser
    parser_object = GPSParser(path_to_gps_data, output_type='print')
    parser_object.start_parser()
