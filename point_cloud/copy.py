import os
import sys
import shutil

src=sys.argv[1]
dest=sys.argv[2]



def copyDirectoryTree(directory, destination, preserveSymlinks=True):
  for entry in os.listdir(directory):
    entryPath = os.path.join(directory, entry)
    if os.path.isdir(entryPath):
      entrydest = os.path.join(destination, entry)
      if os.path.exists(entrydest):
        if not os.path.isdir(entrydest):
          raise IOError("Failed to copy thee, the destination for the `" + entryPath + "' directory exists and is not a directory")
        copyDirectoryTree(entryPath, entrydest, preserveSymlinks)
      else:
        shutil.copytree(entryPath, entrydest, preserveSymlinks)
    else:
      shutil.copy(entryPath,destination)

     
copyDirectoryTree(src,dest)
