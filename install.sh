#!/bin/bash

# install openCV into your anaconda. Uncomment below if you need.
# conda install -c conda-forge opencv

# download model
mkdir ./model
cd ./model
wget https://raw.githubusercontent.com/wellflat/cat-fancier/master/detector/models/cat/cascade.xml
wget https://raw.githubusercontent.com/wellflat/cat-fancier/master/detector/models/cat/cascade_24x24.xml