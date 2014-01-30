#!/usr/bin/env python3

# Script to track the currently focused window.

import collections
import datetime
import re
import subprocess
import time

#xscreensaver-command -watch sends output when the status of the xscreensaver changes

def get_timestamp():
	return datetime.datetime.now()

WINDOW_LIST_RE = re.compile('^(0x[a-f0-9]{8})\s+(\d+)\s+([a-zA-Z0-9_-]+)\s+(.*)')
Window = collections.namedtuple('Window', ['window_id', 'desktop_id', 'title'])

def get_window_pid(window_id):
	# Output format: _NET_WM_PID(CARDINAL): 0x1800024
	output = subprocess.check_output(['xprop', '-id', str(window_id), '_NET_WM_PID']).strip()

	try:
		pid = int(output.split()[-1])
	except IndexError:
		pid = -1

	return pid

def get_current_window():
	# Output format: _NET_ACTIVE_WINDOW(WINDOW): window id # 0x1800024
	window = subprocess.check_output(['xprop', '-root', '_NET_ACTIVE_WINDOW']).strip().split()[-1]

	return int(window, 16)

def get_windows():
	windows = {}
	for line in subprocess.check_output(['wmctrl', '-l'], universal_newlines=True).strip().split('\n'):
		data = WINDOW_LIST_RE.search(line)

		if not data:
			continue

		window_id = int(data.group(1), 16)
		desktop_id = int(data.group(2))
		title = data.group(4)
		windows[window_id] = Window(window_id, desktop_id, title)

	return windows


def main():
	while True:
		window_id = get_current_window()
		windows = get_windows()

		try:
			current_window_data = windows[window_id]
			title = current_window_data.title
		except KeyError:
			title = "Unknown window"

		print(get_timestamp(), current_window_data.title, get_window_pid(current_window_data.window_id))

		time.sleep(1)

if __name__ == '__main__':
	main()