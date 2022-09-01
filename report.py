"""The report module is designed to display a report on the lap time by drivers.

A report on the lap time by drivers in ascending or descending order, or to display statistics for one specific driver.
The module needs a directory with 3 files to work:
- this file contains abbreviations and their decryption,
for example 'DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER'
- the log file contains the start logs for each and the drivers with their abbreviations,
for example 'MES2018-05-24_12:05:58.778'
- the log file contains the end logs for each and the drivers with their abbreviations,
for example 'MES2018-05-24_12:04:45.513'
The processing of the directory with files is carried out in a function build_report,
it takes 2 parameters, the directory itself and the order (by default, it is set by increment).
This function outputs a sheet with a ready-made list of drivers and their lap times (ascending by default).
Next, the data is transmitted to the function 'print_report',
the numbering of drivers takes place in it and the delimiter divides the name of the rider,
the team, the lap time, also the delimiter separates the first 15 drivers and is displayed on the screen
In the function, control of the output of the necessary data from the command line is implemented:
'--files' command and specify the directory, for example --files <folder_path> [--asc | --desc
we will get the statistics on drivers displayed on the screen in ascending order
'--files' command and specify the directory, for example --files <folder_path> --desc
we will get the statistics on drivers displayed on the screen in descending  order
'--driver' of the command and specify the directory, for example --files <folder_path> --driver “Sebastian Vettel”,
we will get statistics displayed on the screen for a specific driver
"""

import argparse
from datetime import datetime
from pathlib import Path

ABBR_FILENAME = 'abbreviations.txt'
START_FILENAME = 'start.log'
END_FILENAME = 'end.log'
DELIMITER_POSITION = 15
LINE_WIDTH = 72


def read_file(filepath):
    """Function accepts filepath and in read lines the file"""
    with open(filepath) as f:
        return f.readlines()


def parse_abbr_lines(row_strings):
    """Function accepts row strings with abbreviations.txt, separates them and collects them into a list"""
    parsed_lines = []
    for line in row_strings:
        parsed_line = line.rstrip().split('_')
        parsed_lines.append(parsed_line)
    return parsed_lines


def parsed_start_end_lines(row_strings):
    """Function accepts row strings with start.log or end.log, separates them into abbr and data time,
    after which collects them into a list
    """
    parsed_lines = []
    for line in row_strings:
        abbr, date_time = line[:3], line[3:].replace('_', ' ').rstrip()
        parsed_lines.append((abbr, datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f')))
    return parsed_lines


def build_report(dir_, desc=False):
    """Construction report based on data from the directory.

       The function accepts the main directory parameter, and desc.
       The directory parameter specifies the name of the directory where the 3 abbreviation files are stored,
       the start time and the end time of the circle. After receiving this data, their processing begins,
       first there is a directory and files in it, then they are parsed and sorted.
       Next, the calculation of the lap time of each driver takes place,
       if the data on the start and end times of the lap are mixed up,
       the function will replace them with places. The function also finds the driver's full data by the abbreviation
       and substitutes it instead of the abbreviation. As a result,
       we will get a list of drivers with the default lap time in ascending order,
       or if a parameter is specified desc=True, in descending order.

       """

    try:
        Path(dir_).resolve()
    except FileNotFoundError:
        print(dir_, 'No such file or directory. Please, input the correct path')
    abbr_filepath = Path(dir_).resolve() / ABBR_FILENAME
    start_filepath = Path(dir_).resolve() / START_FILENAME
    end_filepath = Path(dir_).resolve() / END_FILENAME
    abbr_lines = sorted(parse_abbr_lines(read_file(abbr_filepath)))
    start_lines = dict(sorted(parsed_start_end_lines(read_file(start_filepath))))
    end_lines = dict(sorted(parsed_start_end_lines(read_file(end_filepath))))

    result = []
    for abbr_item, (abbr_st, start_time), (abbr_en, end_time) in zip(abbr_lines, start_lines.items(),
                                                                     end_lines.items()):
        if abbr_st == abbr_en:
            time_lap = str(end_time - start_time)
            if start_time > end_time:
                time_lap = str(start_time - end_time)
        if abbr_st == abbr_item[0]:
            abbr_st = abbr_item[1], abbr_item[2]
            result.append((*abbr_st, time_lap))
            result.sort(key=lambda x: x[2])
    return result if not desc else sorted(result, key=lambda x: x[2], reverse=True)


def print_report(data):
    """Function print result data.

    The print function takes the date and numbers the drivers sequentially,
     and divides the driver's name, team and time with a delimiter. also,
      the delimitor separated the 15 first drivers from the subsequent ones.
    """
    for index, item in enumerate(data, start=1):
        print(f'{index}. {item}'.replace(',', ' | '))
        if index == DELIMITER_POSITION:
            print('-' * LINE_WIDTH)


def drivers_cod_name(data):
    """ Function create dict with key(Abbr) and value(name driver)."""
    parsed_lines = []
    for line in data:
        key = str("".join(e[0] for e in str(line[0]).split()) + "".join(e[0] for e in str(line[1]).split()))[0:3]
        value = line[0]
        parsed_lines.append((key, value))
    return parsed_lines


def find_driver_and_print_report(data, driver):
    """Function takes two arguments date and driver.

    It filters the drivers available in the date, finding the right one displays statistics.
    If the driver's name was entered incorrectly, an error appears NameError.
    """
    filterated_date = list(filter(lambda item: item[0] == driver, data))
    if not filterated_date:
        raise NameError("Please, check the name of the pilot, enter a valid name. Example 'Sebastian Vettel' ")
    print(filterated_date[0])


def main():
    """Management is assembled here CLI."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='?', type=str, const='build_report', required=True, help='folder path')
    parser.add_argument('--driver', nargs='?', type=str, help='statistic about driver')
    parser.add_argument('--desc', default=False, action="store_true", help='list of drivers order is desc')
    parser.add_argument('--drivers_name', nargs='?', const='drivers_cod_name', type=str,
                        help='abbreviate and name driver')
    args = parser.parse_args()
    result = build_report(args.files, args.desc)
    if args.driver:
        find_driver_and_print_report(result, args.driver)
    if args.drivers_name:
        drivers_cod_name(result)
    else:
        print_report(result)


if __name__ == "__main__":
    main()
