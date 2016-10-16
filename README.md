# Fix luminometer reading orientation
Some plates were put in the luminometer in the wrong orientation, resulting in output (in MS Excel files) flipped around 180 degrees.

This program reads in a table (luminometer readings of a 384-well plate) from the first sheet of a MS Excel file, rotates it 180 degrees, and converts it to the final format expected by the analysis software, a three-column table with the following variables:

- Plate barcode
- Well location
- Luminometer reading value

#### For command line usage run:
```
python fix_plate_readings.py --help
```
