#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd $SCRIPT_DIR

find ./static_resources/uploads/ -mmin +5 -exec rm -f {} \;
