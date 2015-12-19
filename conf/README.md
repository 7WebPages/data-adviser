# Install

    sudo pip install --upgrade git+https://github.com/ansible/ansible.git@devel
    sudo pip install 'dopy>=0.3.6,<=0.3.6'
    sudo pip install httplib2

# Vagrant

    vagrant plugin install vagrant-hostsupdater
    vagrant plugin install vagrant-cachier

*Ansible 2.0 Issues related to this project*:

 - https://github.com/ansible/ansible-modules-core/issues/2509
 - https://github.com/ansible/ansible-modules-core/issues/1412

# MacOS local setup

    brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb

**Edit encrypted config**

    ansible-vault edit conf/env_vars/private.yml --vault-password-file conf/password.txt

**Deploy to vagrant**

    ansible-playbook -i development site.yml --vault-password-file password.txt

**Deploy to digitalocean**

    ansible-playbook -i production site.yml --vault-password-file password.txt

**Create digitalocean servers**

    ansible-playbook -i production digitalocean_create.yml --vault-password-file password.txt -vvvv

**Destroy digitalocean servers**

    ansible-playbook -i production digitalocean_delete.yml --vault-password-file password.txt -vvvv
    
**Rebuild digitalocean servers**

    ansible-playbook -i production digitalocean_rebuild.yml --vault-password-file password.txt -vvvv