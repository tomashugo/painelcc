#!/bin/bash

source /home/tomash/painelcc/painelccenv/bin/activate

if ps -ef | grep -v grep | grep create_meter_history.py ; then
   echo "create meter history ja rodando"
else
   python /home/tomash/painelcc/create_meter_history.py
fi

if ps -ef | grep -v grep | grep update_inspection.py ; then
   echo "update inspection ja rodando"
else
   python /home/tomash/painelcc/update_inspection.py
fi

if ps -ef | grep -v grep | grep update_consumer.py ; then
   echo "update consumer ja rodando"
else
   python /home/tomash/painelcc/update_consumer.py
fi

if ps -ef | grep -v grep | grep create_historico_consumo.py ; then
   echo "histotrico consumo ja rodando"
else
   python /home/tomash/painelcc/create_historico_consumo.py
fi
