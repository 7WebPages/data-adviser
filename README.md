> Know your market (c)

Web based market research tool. Based on thousands personal classified ads, we can put brand value to numbers. Know
your local market, know your customer.

# TODO

    - Asynchronous, non-blocking, extendable web spider (tornado/aiohttp)
    - Ansible playbooks, scalable configuration
    - Django web interface, d3 graphs
    - ElasticSearch data aggregation, Web-based rules editor (separate technical complexity and business needs)
    
# Stack

    - Back-end
        - ElasticSearch (full-text search, data aggregation)
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

![alt tag](https://raw.github.com/7WebPages/data-adviser/master/docs/data_adviser.png)

# Code structure

    - docs          (documentation)
    - src/analytics (web interface)
    - src/collector (data spiders)
    - conf          (asnible playbooks)
    - runtests.py   (runs python and javascript tests)
    
# Installing

    curl -sL https://deb.nodesource.com/setup | sudo bash -
    sudo apt-get install nodejs
    sudo apt-get install build-essential

# Running tests

    make test
