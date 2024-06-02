@echo off
cd ../SRCS && export PYTHONPATH=${PWD} && cd ../TESTS
echo Running ... [ "$@" ]
python "$@"
# pause