import logging

logging.basicConfig(level=logging.INFO,filename="log.log",filemode="w",
                    format=	"%(asctime)s - %(levelname)s - %(message)s")
#W - It indicates that the file should be opened in write mode.
#This runs for only one time so create this log at the beginning of the code.
x = 2
logging.info(f"The value of x is {x}")
#Output - 2024-05-12 17:54:28,509 - INFO - The value of x is 2

try:
    1/0
except ZeroDivisionError as e:
    logging.error("Zerodivisionerror",exc_info=True)
    #Output - 2024-05-12 17:57:37,880 - ERROR - Zerodivisionerror
#Traceback (most recent call last):
 # File "D:\tutorials\python\helperlog.py", line 14, in <module>
  #  1/0
 #   ~^~
#ZeroDivisionError: division by zero

try:
    1/0
except ZeroDivisionError as e:
    logging.exception("test")
    #2024-05-12 18:06:49,510 - ERROR - test
#Traceback (most recent call last):
  #File "D:\tutorials\python\helperlog.py", line 23, in <module>
 #   1/0
 #   ~^~
#ZeroDivisionError: division by zero


logger = logging.getLogger(__name__)
handler = logging.FileHandler('test.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("test the costum logger")
#Output -
#2024-05-12 18:25:49,736 - __main__ - INFO - test the costum logger
#2024-05-12 18:25:49,736 - INFO - test the costum logger


#logging.info("info")
#logging.warning("warning") #Output - WARNING:root:warning
#logging.error("error") #Output - ERROR:root:error
#logging.critical("critical") #Output - CRITICAL:root:critical





#Link for searching for some more attributes:
# https://docs.python.org/3/library/logging.html#logging-levels
# Youtube link: https://www.youtube.com/watch?v=urrfJgHwIJA