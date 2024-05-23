# update
setup.py

git push

# create zip file by below command
python3 setup.py sdist

create wheel file using below command
python3 setup.py bdist_wheel

# upload in pypi
pip3 install twine
twine upload dist/*

done. 