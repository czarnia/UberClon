cd ./test/AppServer
py.test --cov=./
cd ../..
mv ./test/AppServer/.coverage .coverage
