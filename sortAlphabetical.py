from os import stat, utime, walk
from datetime import datetime, timedelta

# printing the list using loop
def set_file_last_modified(filepath, dt):
    dtepoch = dt.timestamp()
    utime(filepath, (dtepoch, dtepoch))

# get files from our folder
mypath = './junk'
files = next(walk(mypath), (None, None, []))[2]  # [] if no file
print('Sorting folder '+mypath)

# sort our files alphabetically
files.sort()
# subtract the number of files in seconds
settime = datetime.now() - timedelta(seconds=len(files))

# printing the list using loop
for currentfile in range(len(files)):
    set_file_last_modified(mypath+'/'+files[currentfile], settime + timedelta(seconds=1))
    print(files[currentfile])
