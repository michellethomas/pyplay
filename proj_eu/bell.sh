#!/bin/bash

while [ 1 ] 
  do
    sleep $[ ( $RANDOM % 10 )  + 1 ]
    /usr/bin/printf "\a"
  done
