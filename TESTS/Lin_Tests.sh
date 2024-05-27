#! /bin/bash
cd ../SRCS && export PYTHONPATH=${PWD} && cd ../TESTS
fullstamp=$(date '+%Y-%m-%d_%k-%M-%S')
echo "Testing ... [ py4cli ]"
echo "****************************************************************************************"
coverage run --source=../../py4cli/SRCS -m pytest --template=html1/index.html --report=../REPORTS/TestCaseResults.html > ../REPORTS/run_${fullstamp}.txt
if [ $? == 0 ]
then 
       echo "Test Execution Completed"
fi
coverage html -d ../REPORTS/htmlcov
echo "****************************************************************************************"
echo "Check Log file ... [ ..\REPORTS\run_${fullstamp}.txt ]"
echo "Check Test Execution Results ... [ ..\REPORTS\TestCaseResults.html ]"
echo "Check Test Execution Coverage ... [ ..\REPORTS\htmlcov ]"
echo "****************************************************************************************"
# pause