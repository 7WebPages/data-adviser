# e-Commerce market research tool

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
        - Apache Cassandra 3.0 (NoSQL storage)
        - Django 1.8
        - Spider
    - Front-end
        - webpack / jslint / mocha
    - Deployment
        - Ansible
    - Continuous integration (?)

# Architecture

# Code structure

    - src/analytics (web interface)
    - src/collector (data spiders)
    - conf          (asnible playbooks)
    - runtests.py   (runs python and javascript tests)