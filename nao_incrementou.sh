#!/bin/bash
if ps -ef | grep -v grep | grep nao_incrementou.py ; then
   echo "processo ja rodando"
   exit 0
else 
   source /home/tomash/painelcc/painelccenv/bin/activate
   python /home/tomash/painelcc/nao_incrementou.py
fi
