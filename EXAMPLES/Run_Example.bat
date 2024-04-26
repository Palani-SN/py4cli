@echo off
set PYTHONPATH=..\SRCS;%PYTHONPATH%
echo Running ... [ %* ]
python %*
pause