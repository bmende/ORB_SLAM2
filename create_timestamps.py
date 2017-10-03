#################################
# Expects the images to be named in numerical order from first to last
# e.g. 0001.png, 0002.png, 0003.png, ..., 1234.png, 1235.png
#############################

import time
import datetime
import sys, os


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print "Usage: python create_timestamps.py [image_directory] [frame_rate (def 30fps)]"
        exit(1)

    directory = sys.argv[1]
    frame_rate = 30
    if len(sys.argv) == 3:
        frame_rate = int(sys.argv[3])
    delta = 1/float(frame_rate)
    now_timestamp = time.mktime(datetime.datetime.now().timetuple())
    print "Now is:", now_timestamp
    print "Image Directory:", directory
    print "Frame Rate:", frame_rate, delta

    image_files_list = sorted(os.listdir(directory))

    with open('timestamps.txt', 'w') as timestamp_file:
        for i, image_file in enumerate(image_files_list):
            line = str(now_timestamp + i*delta) + " " + os.path.join(directory, image_file) + "\n"
            timestamp_file.write(line)
