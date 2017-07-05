#!/bin/bash

source /home/tomash/painelcc/painelccenv/bin/activate

if ps -ef | grep -v grep | grep update_alvos_abertos.py ; then
   echo "alvos abertos ja rodando"
else
   python /home/tomash/painelcc/update_alvos_abertos.py
fi
