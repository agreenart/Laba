from data import OfficeWorkers

ERROR_IO = 1
ERROR_VALUE = 2

def load_fp_from_file(file_name):
    fp_list = []
    try:
        file = open(file_name, 'r')

    except IOError:
        print("I/O Error")
        exit(ERROR_IO)
    for line in file:
        try:
            fp_list.append(OfficeWorkers(*line.replace('\n', '').split(';')))
        except ValueError as err:
            print("Broken Data on line ", line, " Here is error: ", err)
            file.close()
            exit(ERROR_VALUE)
        except TypeError as err:
            print("Broken Data on line ", line, " Here is error: ", err)
            file.close()
            exit(ERROR_VALUE)
    file.close()
    return fp_listc