today =`date '+%Y-%m-%d  %H:%M:%S'`

update:
	cd ~/scripts/vk_sheety_posts
	python3 remake_posts_dump.py

push:
	cd ~/scripts/vk_sheety_posts
	python -m black .
	git add .
	git commit -m "autocommit $(today)"
	git push origin main
	
setup:
	cd ~/scripts/vk_sheety_posts
	pip3 install -r ./misc/requirements.txt
	python3 back/crontab_manager.py start
	
start:
	cd ~/scripts/vk_sheety_posts
	python3 app.py

stop:
	cd ~/scripts/vk_sheety_posts
	python3 back/crontab_manager.py stop