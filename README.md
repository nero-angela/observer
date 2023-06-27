# Observer
This project is made in Python3 and will send you a discord webhook when your server is down.

# How to start
1. Add VirtualEnv and install requirements.
```
make init
```

2. Create `.env` in root directory.
```
API_URLS=https://YOUR_SERVER1,https://YOUR_SERVER2
API_NAMES=YOUR_SERVER_NAME1,YOUR_SERVER_NAME2
DISCORD_WEBHOOK_URL=YOUR_WEBHOOK_URL
```

3. Run in background.
```
make run
```

4. Stop running.
```
make stop
```
