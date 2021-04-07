#!/bin/bash

rm -rf report

mkdir -p report

rm -rf allure-report

pytest tests --reportportal

/usr/local/bin/allure/bin/allure generate report

sudo docker-compose -f docker-compose-v3.yml down

