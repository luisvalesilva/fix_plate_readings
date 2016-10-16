#!/usr/bin/env python

"""Rotate a table in MS Excel file."""

import utils
import pandas as pd
import time
import os
from colorama import Fore, Back, Style, init
init(autoreset=True)

def fix_plate_readings(inputFile, barcode):
#def fix_plate_readings(inputFile):
    """
    Given a MS Excel file with a table (readings from a 386-well plate), rotates the
    well positions clockwise by the indicated degree.

    Keyword arguments:
    :param inputFile: path to MS Excel file (no default)
    :param barcode: plate barcode (no default)
    :param loessSpan: degree of rotation of table (default: 180)
    :return: Table in the original, rotated and tidy (vertical) formats in a MS Excel file
    """
    t0 = time.time()
    
    # Read table from MS Excel file and get file path details
    table = pd.read_excel(io=inputFile, sheetname=0, header=0, index_col=0)
    dir_name, file_name, extless_filename = utils.get_filename_from_path(inputFile)
    print('Read table from file:\n"{}"'.format(file_name))
    print()
    
    # Rotate table 180 degrees
    rotated_table = utils.rotate_table(df=table)
    
    # Get barcode from user
    # Added as CLI argument instead
    #print()
    #barcode = (input(Fore.RED + 'What is the plate\'s barcode: '))
    #print(Style.RESET_ALL)
    
    # Convert to tidy format
    tidy_table = utils.rectangular_to_tidy(df=rotated_table, barcode=barcode)
    
    # Write to MS Excel file
    file_name = os.path.basename(file_name)
    writer = pd.ExcelWriter(dir_name + '/' + extless_filename + '_final.xlsx')
    tidy_table.to_excel(writer,'Final table', index=False)
    rotated_table.to_excel(writer,'Rotated table')
    table.to_excel(writer,'Original table')
    writer.save()
    
    print()
    print(Fore.CYAN + 'Saved final tables to MS Excel file:\n"{}_final.xlsx"'.format(extless_filename))
    print()
    utils.print_elapsed_time(t0)


def main():
    print()
    print(Style.BRIGHT + "---------------------------------------------")
    print(Style.BRIGHT + "        ROTATE TABLE IN MS EXCEL FILE")
    print(Style.BRIGHT + "---------------------------------------------")
    print()
    fix_plate_readings(inputFile=args.inputFile, barcode=args.barcode)
    #fix_plate_readings(inputFile=args.inputFile)
    print(Style.BRIGHT + "---------------------------------------------")
    print()


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=("Rotates a table in MS Excel file and puts it in tidy format" +
                                                  " (takes table in the first sheet in Excel file)."))
    parser.add_argument('-i','--inputFile', help='path to MS Excel file', required=True)
    parser.add_argument('-b','--barcode', help='plate barcode', required=True)
    args = parser.parse_args()
    
    main()
