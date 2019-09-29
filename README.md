# HPC Homework 2: Parallelism vs Concurrency

## Setup
There is a `filelist.txt` included in the project. Before running the python files, make sure to create big files in the same directory as the project and name them following the `filelist.txt`. For example, `filelist.txt` now contains 4 rows - filename.txt, filename1.txt, filename2.txt, filename3.txt, so make sure to create 4 such files. To create a big file you can do.
```bash
dd if=/dev/zero of=filename.txt count=1024000 size=1024
```

## Running
After making sure you have all the necessary files created you can run `proc.py` or `thread.py` the following way:
```bash
time python3 <filename>.py
```
This will run python3 interpreter and time the execution of the program using time command.

## Warning!
Make sure to remove the `dest` folder before running one of the programs again.