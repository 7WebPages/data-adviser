# Data Analyzer

[![Build Status](https://travis-ci.org/7WebPages/data-adviser.svg?branch=master)](https://travis-ci.org/7WebPages/data-adviser)
[![Build Status](https://codecov.io/github/7WebPages/data-adviser/coverage.svg?branch=master)](https://codecov.io/github/7WebPages/data-adviser?branch=master)

![alt tag](https://raw.github.com/7WebPages/data-adviser/master/docs/data-everywhere.png)

> Know your market (c)

Web based market research tool. Based on thousands personal classified ads, analyzed and put together in beautiful 
interface. We put this data into real numbers, real value. Know your market, know your customer.

# TODO

    - Asynchronous, non-blocking, extendable web spider (tornado/aiohttp)
    - Ansible playbooks, scalable configuration
    - Django web interface, d3 graphs
    - ElasticSearch data aggregation, Web-based rules editor (separate technical complexity and business needs)
    
# Stack

    - Back-end
        - ElasticSearch 2 (full-text search, data aggregation)
        - Apache Cassandra 3.0 (NoSQL storage, intermediate/aggregated data)
        - Django 1.8
        - Spider
    - Front-end
        - webpack / jslint / mocha / d3
    - Deployment
        - Ansible
    - Continuous integration
        - Travis CI

# Architecture

![alt tag](https://raw.github.com/7WebPages/data-adviser/master/docs/data-adviser.png)

# Code structure

    - docs          (documentation)
    - conf          (asnible playbooks)
    - src/analytics (web interface)
    - src/collector (data spiders)
    - runtests.py   (runs python and javascript tests)
    
# Installing

    curl -sL https://deb.nodesource.com/setup | sudo bash -
    sudo apt-get install nodejs
    sudo apt-get install build-essential
    sudo npm install

# Running tests

    make test
