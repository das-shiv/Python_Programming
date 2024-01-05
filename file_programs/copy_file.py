# copyfile() = copies the content of the file, copy() = copyfile() + permissions + destination can be a directory, copy2() = copy() + metadata of the file
import shutil

shutil.copy("file.txt", "copyfile.txt" )


