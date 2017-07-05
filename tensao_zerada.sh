#!/bin/bash

if ps -ef | grep -v grep | grep tensao_zerada.py ; then
   echo "processo ja esta rodando"
   exit 0
else
   source /home/tomash/painelcc/painelccenv/bin/activate  
   python /home/tomash/painelcc/tensao_zerada.py
fi
