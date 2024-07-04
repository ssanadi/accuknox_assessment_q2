import psutil
import time
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def log_message(message):
    print(message)
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_message(f"ALERT: High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_message(f"ALERT: High memory usage detected: {memory_usage}%")

def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    disk_usage_percent = disk_usage.percent
    if disk_usage_percent > DISK_THRESHOLD:
        log_message(f"ALERT: High disk usage detected: {disk_usage_percent}%")


#Check health after every minute
while True:
    log_message("Checking system health...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    log_message("System health check complete.\n")
    time.sleep(60)
