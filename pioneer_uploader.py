"""
Upload generated program to drone
"""
import os
import sys
import time
from pioneer_sdk import Pioneer
import logging


def main():
    try:
        file_path, ip, port, mode = sys.argv[1:5]
    except ValueError:
        logging.error("Invalid arguments")
        return

    if not os.path.exists(file_path):
        logging.error("Can not find program file")
        return

    drone = Pioneer(
        ip=ip,
        mavlink_port=port,
        connection_method="udpout" if mode == "wifi" else "serial",
        logger=True,
    )

    try:
        drone.lua_script_upload(file_path)
        time.sleep(2)
        drone.close_connection()
    except Exception as e:
        logging.error(e)
        return


if __name__ == "__main__":
    main()
