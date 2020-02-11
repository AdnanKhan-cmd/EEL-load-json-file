from __future__ import print_function	# For Py2/3 compatibility
import eel
import json

with open('json.json') as f:
    d = json.load(f)

# Set web files folder
eel.init('web')

eel.say_hello_js((d))   # Call a Javascript function

eel.start('index.html', size=(300, 200))    # Start
