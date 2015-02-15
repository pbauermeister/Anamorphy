#!/bin/sh

set -e

echo
echo "Building for Debian"
echo "==================="

###############################################################################
# STEP 1 - Cleanup
echo
echo "= Cleaning up ="
./clean.sh
rm -rf deb_dist/

###############################################################################
# STEP 2 - PEP8 check
echo
echo "= PEP 8 ="
# ./check_pep8.sh

###############################################################################
# STEP 3 - Debian build
echo
echo "= Debian build ="
python setup.py --command-packages=stdeb.command bdist_deb
