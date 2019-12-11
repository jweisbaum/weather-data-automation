#!/bin/bash

set -e

pushd /usr/local/src
curl https://sats.nws.noaa.gov/~degrib/download/degrib-src.tar.gz | tar zx
pushd /usr/local/src/degrib/src
ls -al
./config-linux.sh
set +e
make
set -e
cp -v /usr/local/src/degrib/src/degrib/degrib /usr/bin/degrib
chmod +x /usr/bin/degrib
popd
rm -Rf degrib
