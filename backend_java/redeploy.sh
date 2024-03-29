#!/bin/sh
mvn clean
mvn package
pm2 restart all
echo "All done"