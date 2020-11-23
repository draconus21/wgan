#!/bin/bash

#   ________    ________  ______    __  __   ______   ______
#  /_______/\  /_______/\/_____/\  /_/\/_/\ /_____/\ /_____/\
#  \::: _  \ \ \__.::._\/\:::_ \ \ \ \ \ \ \\:::_:\ \\:::_ \ \
#   \::(_)  \ \   \::\ \  \:(_) ) )_\:\_\ \ \  /_\:\ \\:\ \ \ \
#    \:: __  \ \  _\::\ \__\: __ `\ \\::::_\/  \::_:\ \\:\ \ \ \
#     \:.\ \  \ \/__\::\__/\\ \ `\ \ \ \::\ \  /___\:\ '\:\/.:||
#      \__\/\__\/\________\/ \_\/ \_\/  \__\/  \______/  \_____/
#
# Copyright (c) 2015-20 Airy3D Inc.
# All rights reserved.

# ------------------------------------------------------------------- #
#                                 ARGS                                #
# ------------------------------------------------------------------- #
SRC_DIR=""

A3D_SOURCE_ENVS=1
OPTIND=1
OPTSPEC=":h-:"
while getopts "$OPTSPEC" optchar; do
    case "${optchar}" in
        -)  case "${OPTARG}" in
                src_dir=*) SRC_DIR=${OPTARG#*=} ;;
                *) echo "Unknown argument: '--${OPTARG}', run 'source env.sh -h' to see the available args"; return 1;
            esac;;

        h)  help="  -h: Print this message\n"
            help+="  --src_dir=<path>: path to source dir on the local machine\n"
            printf "%b" "usage: source env.sh <options> \n$help\n"
            return 0
            ;;

        ?)  echo "Unknown argument: '-${OPTARG}', run 'source env.sh -h' to see the available args"; return 1;
            ;;
    esac
done

# ------------------------------------------------------------------- #
#                               VARIABLES                             #
# ------------------------------------------------------------------- #
if [[ -z "$SRC_DIR" ]]; then
    echo "Warning: src_dir is empty, assuming current dir is src_dir: $(pwd)";
    SRC_DIR="$(pwd)"
fi


export SRC_DIR

PYTHONPATH="$SRC_DIR/src"

PATH=$PYTHONPATH:$PATH

export PATH
export PYTHONPATH
