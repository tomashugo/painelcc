#!/bin/bash

if ps -ef | grep -v grep | grep parsing.py ; then
   echo "processo ja rodando"
   exit 0
else
   source /home/tomash/painelcc/painelccenv/bin/activate
   python /home/tomash/painelcc/parsing.py &
fi
