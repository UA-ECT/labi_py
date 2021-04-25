import csv
import time
import psutil

def main () :
    fout = open ("net.csv", "w")
    writer = csv.DictWriter (fout, delimiter=":", fieldnames=["time", "sent", "recv", "cpu"])
    writer.writeheader()

    for i in range(0,10) :
        cpu = psutil.cpu_percent (interval=1)
        tm = time.time()
        net = psutil.net_io_counters()
        data = {"time": tm, "sent": net[0], "recv": net[1],"cpu": cpu }
        print(data)
        writer.writerow(data)
        time.sleep(1)

