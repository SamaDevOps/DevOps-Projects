#! /bin/bash

echo "Enter a number"
read number

if [ $number -lt 10 ]
then
    echo number is lower than 10
else
    echo number is greater than 10
fi

if [ -s $1 ]
then
  echo file is not empty
else
  echo file is empty
fi
