import os
import csv
import time
import argparse
import telnetlib
from datetime import datetime

# 测试远程服务端口连接耗时
# python3 windows_telnet.py 10.158.133.211 80

parser = argparse.ArgumentParser()
parser.add_argument("ip", type=str, help="ip")
parser.add_argument("port", type=str, help="port")
args = parser.parse_args()

timeFormat = "%Y-%m-%d %H:%M:%S.%f"

starTimeTitle = "开始连接时间"
endTimeTitle = "结束连接时间"
differenceTimeTitle = "连接总耗时"

while True:
    starTime = datetime.now()
    starTimeView = starTime.strftime(timeFormat)
    print("开始连接:{0}".format(starTimeView))
    tn = telnetlib.Telnet(args.ip, args.port)
    endTime = datetime.now()
    endTimeView = endTime.strftime(timeFormat)
    print("连接完成:{0}".format(endTimeView))
    tn.close()
    print("连接结束")
    differenceTime = endTime - starTime
    print("连接消耗:{0}".format(differenceTime))
    nowTime = datetime.now()
    csvFileName = "{0}.csv".format(nowTime.strftime("%Y-%m-%d"))
    if os.path.exists(csvFileName) is not True:
        with open(csvFileName, "w", encoding="utf-8", newline="") as csvfile:
            fieldnames = [starTimeTitle, endTimeTitle, differenceTimeTitle]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    with open(csvFileName, "a", encoding="utf-8", newline="") as csvfile:
        fieldnames = [starTimeTitle, endTimeTitle, differenceTimeTitle]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({starTimeTitle: starTimeView,
                         endTimeTitle: endTimeView,
                         differenceTimeTitle: differenceTime})

    time.sleep(0.2)
