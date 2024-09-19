"""
Rewrite 12th program to capture log using 'logging' library
"""

print("Configure logger and TESTING our logger")
print("-"*20)
# ------------

import logging

my_logger = logging.getLogger(__name__) # __name__ = '__main__'
logging.basicConfig(filename='my_20th_program.log', level=logging.INFO, filemode="w", format="%(levelname)s : %(filename)s : %(asctime)s : %(message)s")

my_logger.info("THIS IS FOR TESTING OUR LOGGER")
my_logger.info("This is info")
my_logger.debug("This is debug")
my_logger.warning("This is warning")
my_logger.critical("This is critical")
my_logger.error("This is error")
my_logger.info("THIS IS END TESTING OUR LOGGER")

print("#"*40, end="\n\n")
#################################

print("Get data from log_report_4.json")
print("-"*20)
# ------------
try:
    my_logger.info("Opening log_report_4.json")
    my_json_file_handle = open("log_report_4.json", "r")
    my_logger.info("Opening log_report_4.json SUCCESS")
except FileNotFoundError:
    my_logger.error("Not able to open file. So exiting")
    exit()
else:
    try:
        my_logger.info("Importing json library")
        import json
        my_logger.info("Importing json library success")
    except ModuleNotFoundError:
        my_logger.error("Not able to import json")
        my_logger.error("Exiting..")
        exit()
    else:
        my_logger.info("Reading json file")
        json_file_content = json.load(my_json_file_handle)
        my_logger.info("Reading json file Success")
    finally:
        my_logger.info("closing json file")
        my_json_file_handle.close()
        my_logger.info("Closing json file completed")

print("json_file_content:", json_file_content, sep="\n", end="\n\n")
print("type of json_file_content:", type(json_file_content), sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#################################

print("Write to log_report_5.txt")
print("-"*20)
# ------------

my_logger.info("Writing to log_report_5.txt")
try:
    my_logger.info("Started writing to file")
    my_txt_file_handle = open("log_report_5.txt", "w")
    print("IP", "DATE", "PICS", "URL", sep="\t", file=my_txt_file_handle)
    for i, j, k, l in json_file_content.values():
        print(i, j, k, l, sep="\t", file=my_txt_file_handle)
    my_txt_file_handle.close()
    my_logger.info("Writing completed and log_report_5.txt created")
    print("log_report_5.txt created, Please check")
except Exception as e:
    my_logger.error('Got error while writing. So exiting')
    exit()

print("#"*40, end="\n\n")
#################################

print("\nlog file my_20th_program.log created, please check\n")