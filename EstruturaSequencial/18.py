sizeM = float(raw_input("File size (MB): "))
vel = float(raw_input("Velocity dowload (Mbps): "))

sizeBits = sizeM * 1024 * 1024 * 8
timeM = (sizeBits / (vel * 1024 * 1024)) / 60

print "Download time (minutes): ", timeM