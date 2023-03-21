#!/usr/bin/env bash

set -eu

while ! nc -vz mariadb 3306 1>&2 2>/dev/null; do
  sleep 1
done

"$@"
