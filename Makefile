init:
	@python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run:
	@. .venv/bin/activate && nohup python observer.py > log.txt 2>&1 &

stop:
	@pkill -f observer.py
