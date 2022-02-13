import pyshark
import datetime

date = datetime.datetime.now()
file = "YourPathHere/Captures/" + str(date.strftime("%B"))  + "/" + str(date.year) + "-" + str(date.month) + "-" + str(date.day) + ".cap"
output = open(file, "w")
time = 86399
capture = pyshark.LiveCapture(interface="en0", output_file=file)
capture.sniff(timeout=time)
output.close()
