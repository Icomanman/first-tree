# This is in python 2
import os
import sys
import pywinauto as pw
import time

press = pw.keyboard.send_keys


def main(process=None, timeout=3):
    # timeout in seconds
    print "The process id is: %s" % process
    if process == None:
        game = pw.Application().connect(title="The First Tree")
    else:
        game = pw.Application().connect(process=process)

    if game == None:
        return None

    dlg = game["The First Tree"]
    dlg.set_focus()
    time.sleep(timeout)
    press("{W down}")

    return type(game)


if len(sys.argv) > 1:
    main(int(sys.argv[1]))
else:
    main()
