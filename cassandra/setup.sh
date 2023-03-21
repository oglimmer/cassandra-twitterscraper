#!/usr/bin/env bash

set -eu

apt update && apt upgrade -y
apt install curl -y
apt install gnupg -y
apt install openjdk-11-jre-headless -y
echo "deb https://debian.cassandra.apache.org 41x main" | tee -a /etc/apt/sources.list.d/cassandra.sources.list
curl https://downloads.apache.org/cassandra/KEYS | apt-key add -
apt update
apt install cassandra -y
