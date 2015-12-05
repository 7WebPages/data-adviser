# Install

sudo pip install --upgrade git+https://github.com/ansible/ansible.git@devel
sudo pip install 'dopy>=0.3.6,<=0.3.6'
sudo pip install httplib2

Issues:
    https://github.com/ansible/ansible-modules-core/issues/2509
    https://github.com/ansible/ansible-modules-core/issues/1412

# MacOS
brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb

ansible-playbook -i development site.yml --ask-vault-pass
ansible-playbook -i production site.yml --ask-vault-pass

ansible-vault edit env_vars/private.yml

ansible-vault edit conf/env_vars/private.yml --vault-password-file conf/password.txt

ansible-playbook -i development site.yml --vault-password-file password.txt
ansible-playbook -i production site.yml --vault-password-file password.txt

ansible-playbook -i production digitalocean_create.yml --vault-password-file password.txt -vvvv
ansible-playbook -i production digitalocean_delete.yml --vault-password-file password.txt -vvvv