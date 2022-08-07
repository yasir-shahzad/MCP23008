# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MCP23008
# This code is designed to work with the MCP23008_REG_I2CR8G5LE_10A I2C relay controller available from ControlEverything.com.
# https://www.controleverything.com/content/Relay-Controller?sku=MCP23008_REG_I2CR8G5LE_10A#tabs-0-product_tabset-2

import time

from MCP23008 import MCP23008
mcp23008 = MCP23008()

while True :
	mcp23008.select_relay()
	mcp23008.set_output_dir()
	mcp23008.checking_status()
	mcp23008.gpio_config()
	mcp23008.check_status()
	print " ******************************* "
	time.sleep(0.2)
