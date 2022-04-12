today =`date '+%Y-%m-%d  %H:%M:%S'`

push:
	cd ~/scripts/vk_sheety_posts
	python -m black .
	git add .
	git commit -m "autocommit $(today)"
	git push origin master
	
setup:
	cd ~/scripts/vk_sheety_posts
	pip3 install -r ./misc/requirements.txt
	python3 ./crontab_manager.py start
	
start:
	cd ~/scripts/vk_sheety_posts
	echo 'None'

stop:
	cd ~/scripts/vk_sheety_posts
	python3 ./crontab_manager.py stop