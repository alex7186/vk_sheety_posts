today =`date '+%Y-%m-%d  %H:%M:%S'`
commit_name = "autocommit $(today)"

push:
	@cd ~/scripts/vk_sheety_posts
	@python -m black .
	@git add .
	@git commit -m $(commit_name)
	@git push origin main
	@echo "\n✅ succussfully pulled as $(commit_name)"
	
setup:
	@cd ~/scripts/vk_sheety_posts
	@pip3 install -r ./misc/requirements.txt
	@python3 back/crontab_manager.py start
	
start:
	@cd ~/scripts/vk_sheety_posts
	@python3 app.py

stop:
	@cd ~/scripts/vk_sheety_posts
	@python3 back/crontab_manager.py stop

update:
	@cd ~/scripts/vk_sheety_posts
	@python3 remake_posts_dump.py