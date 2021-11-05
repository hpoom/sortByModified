from os import stat, utime, walk
from datetime import datetime, timedelta

# printing the list using loop
def set_file_last_modified(filepath, dt):
    dtepoch = dt.timestamp()
    utime(filepath, (dtepoch, dtepoch))

# get files from our folder
#mypath = './junk'
mypath = '/Volumes/PSP-1000/ISO/CAT_PSP Games'
files = next(walk(mypath), (None, None, []))[2]  # [] if no file
print('Sorting folder '+mypath)

# sort our files alphabetically
files.sort()
# subtract the number of files in seconds
settime = datetime.now() - timedelta(minutes=len(files))

# printing the list using loop
for currentfile in range(len(files)):
    settime += timedelta(minutes=1)
    set_file_last_modified(mypath+'/'+files[currentfile], settime)
    print(files[currentfile])

# sudo dot_clean -m -v /Volumes/PSP-1000
