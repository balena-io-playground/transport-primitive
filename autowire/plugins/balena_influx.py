import os

SERVICE_NAME = "influxdb"

def invoke(serviceList):
    if(SERVICE_NAME in serviceList):
        print("Loading {name} plugin".format(name=SERVICE_NAME))
        return getConfigSection()

def getConfigSection():
        host = os.environ.get('INFLUXDB_HOST') or "http://127.0.0.1:8086"
        database = os.environ.get('INFLUXDB_DATABASE') or "balena"
        timeout = os.environ.get('INFLUXDB_TIMEOUT') or "1s"

        output = """
[[outputs.influxdb]]
    urls = ["{url}"]
    database = "{db}"
    timeout = "{to}"
        """.format(url=host, db=database, to=timeout)

        return output