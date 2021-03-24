#!/bin/bash
rm -rf report

mkdir -p report

rm -rf allure-report

pytest tests

/usr/local/bin/allure/bin/allure generate report
