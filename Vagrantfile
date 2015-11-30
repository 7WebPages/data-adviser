VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    config.vm.provider "virtualbox" do |v|
        v.memory = 256
        v.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
    end

    # Django
    config.vm.define "web1" do |app|
        app.vm.hostname = "data-web1.dev"
        app.vm.box = "ubuntu/trusty64"
        app.vm.network :private_network, ip: "192.168.61.4"
        app.vm.network "forwarded_port", guest: 22, host: 2227, id: 'ssh'
    end

    # Celery & queue server (Redis)
    config.vm.define "celery1" do |app|
        app.vm.hostname = "data-celery1.dev"
        app.vm.box = "ubuntu/trusty64"
        app.vm.network :private_network, ip: "192.168.61.5"
        app.vm.network "forwarded_port", guest: 22, host: 2227, id: 'ssh'
    end

    # PostgreSQL (db) & Apache Cassandra (Cache)
    config.vm.define "db1" do |app|
        app.vm.hostname = "data-db.dev"
        app.vm.box = "ubuntu/trusty64"
        app.vm.network :private_network, ip: "192.168.61.6"
        app.vm.network "forwarded_port", guest: 22, host: 2227, id: 'ssh'
    end

    # collector
    config.vm.define "collector1" do |app|
        app.vm.hostname = "data-collector.dev"
        app.vm.box = "ubuntu/trusty64"
        app.vm.network :private_network, ip: "192.168.61.7"
        app.vm.network "forwarded_port", guest: 22, host: 2227, id: 'ssh'
    end

    # Elasticsearch
    config.vm.define "elastic1" do |app|
        app.vm.hostname = "data-elastic.dev"
        app.vm.box = "ubuntu/trusty64"
        app.vm.network :private_network, ip: "192.168.61.8"
        app.vm.network "forwarded_port", guest: 22, host: 2227, id: 'ssh'
    end

end