.PHONY: config deployconfig

ifeq (, $(shell which editor))
$(error "No editor in $(PATH), consider symlinking vim, emacs or nano.")
endif

config: tasks/settings/db.py
deployconfig: tasks/settings/email.py

tasks/settings/db.py: tasks/settings/db.py.base
	cp tasks/settings/db.py.base tasks/settings/db.py
	editor tasks/settings/db.py

tasks/settings/email.py: tasks/settings/email.py.base
	cp tasks/settings/email.py.base tasks/settings/email.py
	editor tasks/settings/email.py

# vim: set noet:
