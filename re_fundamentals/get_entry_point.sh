#!/bin/bash

if [[ -f "./messages.sh" ]];
then
    source ./messages.sh
else
    echo "The file(messages.sh) isn't found" >&2
    exit 1
fi

if [[ $# -eq 0 ]];
then
    echo "Usage: $0 <elf_file_name>" >&2
    exit 1
fi

file_name="$1"


if [[ ! -f "$file_name" ]];
then
     echo "Error! '$file_name' isn't found" >&2
     exit 1
fi

if ! readelf -h $file_name &>/dev/null;
then    
    echo "Error! '$file_name' isn't ELF" >&2
    exit 1
fi


# Using readelf

magic_number=$(readelf -h "$file_name" | awk -F: '/Magic:/ {print $2}' | xargs)

class=$(readelf -h "$file_name" | awk '/Class:/ {print $2}')

byte_order=$(readelf -h "$file_name" | awk -F': *' '/Data:/ {print $2}')

entry_point_address=$(readelf -h "$file_name" | awk '/Entry point address:/ {print $4}')

display_elf_header_info
