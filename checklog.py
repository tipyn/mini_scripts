# this sucks and looks awful, I want to write a better one that looks way cleaner.

logfile = open("/var/log/system.log", "r")
for line in logfile:
    line_split = line.split()
    print line_split
    list = line_split[0], line_split[1], line_split[2], line_split[4]
    print list
