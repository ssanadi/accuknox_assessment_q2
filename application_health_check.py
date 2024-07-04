import requests
import logging
import time

# Set up logging
logging.basicConfig(filename='app_health_check.log', level=logging.WARNING, format="%(asctime)s - %(levelname)s - %(message)s")

application_url = "http://localhost:8080/"


def check_application_health(application_url):
  try:
    response = requests.get(application_url)
    response.raise_for_status()  # Raise an exception for non-200 status codes
    return True
  except requests.exceptions.RequestException as e:
    logging.warning(f"Error checking application health: {e}")
    return False

#Check health after every minute
while True:
    is_healthy = check_application_health(application_url)
    if is_healthy:
          print(f"Application at '{application_url}' is healthy")
    else:
          print(f"Application at '{application_url}' is unhealthy")
    time.sleep(60)

