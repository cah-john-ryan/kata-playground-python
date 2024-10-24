#!/bin/bash
set -ue

# taken from https://cardinalhealth.atlassian.net/wiki/spaces/~727658700/pages/4138467372/Fixing+CAH+Self+Signed+Certificates

ca_path=${ca_path:-~/CAH-Root-CA-PR1.pem}

# e.g if you need to install for 3.9 and it's not default on your system
# python_bin=python3.9
#
# Also, if you use Poetry for your project, you can try (I haven't tested...)
# python_bin=$(poetry env show -p)/bin/python

python_bin=${python_bin:-$(which python)}

# change this if you need to add cert to something else
# e.g. if you need to add to cert store the `requests` package uses
# set this to "certifi"
certifi=${certifi:-"pip._vendor.certifi"}
if [ ! -f $ca_path ]; then
  echo "$ca_path does not exist."; exit 1
fi

ca_pip_cert=$($python_bin -c "from $certifi import where; print(where())")
ca_pip_cert_backup="${ca_pip_cert}.bak"
if [ -f "$ca_pip_cert_backup" ]; then
  echo "backup already exists! Please remove $ca_pip_cert_backup"; exit 1;
fi

new_ca_linecount=$(echo -n $(wc -l $ca_path) | cut -f1 -d' ')

if (cmp --silent $ca_path <(tail -n "$new_ca_linecount" "$ca_pip_cert")); then
  echo "It appears the cert has already been appended. No changes needed."
else
  cp "$ca_pip_cert" "$ca_pip_cert_backup"
  cat $ca_path >> "$ca_pip_cert"
  echo "Cert has been appended to $ca_pip_cert. Have a nice day!"
fi