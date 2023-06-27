init:
	@python3 -m venv .venv && .venv/bin/pip3 install -r requirements.txt

run:
	@nohup .venv/bin/python observer.py > log.txt 2>&1 && sudo chmod 777 log.txt &

stop:
	@pkill -f observer.py
