VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = "ubuntu/trusty64"
    config.vm.network "forwarded_port", guest: 80, host: 8080
    config.vm.network "forwarded_port", guest: 5555, host: 5555
    config.vm.network "forwarded_port", guest: 22, host: 2227, id: 'ssh'
    config.vm.network :private_network, ip: "192.168.33.15"

    config.vm.provider "virtualbox" do |v|
        v.memory = 1024
    end

    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "conf/vagrant.yml"
        ansible.host_key_checking = false
        ansible.verbose = "v"
    end

end