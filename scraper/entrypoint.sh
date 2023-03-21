#!/usr/bin/env bash

set -eu

echo "Waiting for Cassandra..."

while ! nc -vz cassandra_node1 9042 1>&2 2>/dev/null; do
  sleep 1
done

sleep 10 # wait for setup

echo "Cassandra is ready."

"$@"
