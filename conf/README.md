# MacOS

brew install https://raw.githubusercontent.com/kadwanev/bigboybrew/master/Library/Formula/sshpass.rb

ansible-playbook -i development site.yml --ask-vault-pass
ansible-playbook -i production site.yml --ask-vault-pass
