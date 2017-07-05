#!/bin/bash

if ps -ef | grep -v grep | grep mm_versus_consumo.py ; then
   echo "processo ja rodando"
   exit 0
else
   source /home/tomash/painelcc/painelccenv/bin/activate
   python /home/tomash/painelcc/mm_versus_consumo.py >> saida.txt
fi
