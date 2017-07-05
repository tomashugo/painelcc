#!/bin/bash

if ps -ef | grep -v grep | grep queda_consumo.py ; then
   echo "processo ja rodando"
   exit 0
else
   source /home/tomash/painelcc/painelccenv/bin/activate
   python /home/tomash/painelcc/queda_consumo.py
fi
