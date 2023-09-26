"""
Upload generated program to drone
"""
import os
import sys
import time
import re
from pioneer_sdk import Pioneer
import logging


def main():
    try:
        file_path, ip, port, mode = sys.argv[1:5]

        if not os.path.exists(file_path):
            raise FileNotFoundError("Can not find program file")

        ipv4_pattern = (
            r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\."
            r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        )

        if not re.match(ipv4_pattern, ip):
            raise ValueError("Invalid IP address")

        if not 0 < int(port) <= 65535:
            raise ValueError("Invalid port")

        if mode not in ["wifi", "usb"]:
            raise ValueError("Invalid mode. Choose 'wifi' or 'usb'")

        drone = Pioneer(
            ip=ip,
            mavlink_port=port,
            connection_method="udpout" if mode == "wifi" else "serial",
            logger=True,
        )

        if file_path.split(".")[-1] != "lua":
            file_name = file_path + "/" + file_path.split("/")[-1] + ".lua"
            drone.lua_script_upload(file_name)
        else:
            drone.lua_script_upload(file_path)

        time.sleep(2)
        drone.close_connection()

    except Exception as e:
        logging.error(e)
        logging.info(
            "Please download uploader from "
            '<a href="https://docs.geoscan.aero/ru/master/programming/trik/trik_main.html"> site</a>'
        )
        return


if __name__ == "__main__":
    main()
