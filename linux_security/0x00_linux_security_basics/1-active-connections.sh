#!/bin/bash

if [[ $(id -u) -ne 0 ]]; then
    exit 1
fi

echo -e "State\tRecv-Q\tSend-Q\tLocal Address:Port\tPeer Address:Port\tProcess"
sudo ss -tulnp
