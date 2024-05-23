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

# if error 
# use this.
twine upload dist/* -u __token__ -p pypi-AgEIcHlwaS5vcmcCJDkxZjRkMmQzLWRkN2QtNDY4YS05ZDVlLTIzOTgyYzI4YjE3MAACKlszLCJlMDc2ZmZkZC0yOWYyLTRhYzAtYjYxZC02ZjY0NzlhY2E0ZWQiXQAABiBqWtiSyDwL7WhIwFXCI5r2LjRXmBVLUxAgINzhyajP3g

done. 