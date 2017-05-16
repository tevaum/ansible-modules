test:
	ANSIBLE_KEEP_REMOTE_FILES=1 ANSIBLE_LIBRARY=. ansible-playbook -i hosts test-playbook.yaml -u estevao -k

debug:
	ANSIBLE_LIBRARY=~/Projetos/ansible-modules ansible-playbook -vvvvvvv -i hosts test-playbook.yaml -u estevao -k
