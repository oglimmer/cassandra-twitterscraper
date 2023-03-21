#!/usr/bin/env bash

set -eu

while ! cqlsh cassandra_node1 -e 'SELECT now() FROM system.local' 1>&2 2>/dev/null; do
  sleep 1
done

cqlsh cassandra_node1 -f ./setup.sql
