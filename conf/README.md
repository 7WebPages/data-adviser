# MacOS

brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb

cp conf/ansible.cfg ~/.ansible.cfg

ansible-playbook -i development site.yml --ask-vault-pass
ansible-playbook -i production site.yml --ask-vault-pass

ansible-vault edit env_vars/private.yml

ansible-vault edit conf/env_vars/private.yml --vault-password-file conf/password.txt

ansible-playbook -i development site.yml --vault-password-file password.txt
ansible-playbook -i production site.yml --vault-password-file password.txt