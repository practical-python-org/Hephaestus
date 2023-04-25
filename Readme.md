# Hephaestus
Hephaestus was the god of fire, metalworking, stone masonry, forges and the art of sculpture.
He was the son of Zeus and Hera and married to Aphrodite by Zeus to prevent a war of the gods fighting for her hand.
He was a smithing god, making all the weapons for Olympus and acting as a blacksmith for the gods.

He had his own palace on Olympus where he made many clever inventions and automatons of metal to work for him.
He is similar to Athena in his giving skill and help to mortals – in his case artists.

## Hephaestus-Bot
Hephaestus is a Discord bot that uses Py-Cord. The main purpose of this bot is to maintain logs, enforce moderation
and maintain user information.

### Features:

- **Py-Cord**
  - Py-Cord (https://pycord.dev/) is an actively maintained fork of Discord.py, and boasts a few more modern features. 
- **Cogs**
  - Cogs (https://docs.pycord.dev/en/stable/ext/commands/cogs.html) keep things modular. Don't want a feature? Simply delete or remove the file. 
- **Docker**
  - Built on a Python 3.9 base image, and stripped down to provide a small, lightweight docker image that can be used anywhere. 
  - Volumes allow your database to persist even when updating your bot. 
- **Sqlite3 Database**
  - Fast, simple and easy to use, this DB is built into the very core of the bot. 
- **Cross-platform**
  - we use Pathlib (https://docs.python.org/3/library/pathlib.html), which helps keep all our paths relative to the OS the bot is running on. 
- **Secure**
  - Utilizing a trimmed down, debian docker image allows us to reduce the attack surface of the bot to almost zero.
  - Tokens are taken from either a run argument or in env variables, which are ONLY used during deployment of the bot.

### Installation and Deployment:

##### VM in the cloud
If you are running the bot on a VM in the cloud, I have prepared a simple deployment script that automates the entire workflow

``` bash
ssh -i "SSH_KEY.pem" USER@some.cloud.server.com "cd /srv/ && sudo rm -r Hephaestus && sudo git clone https://github.com/practical-python-org/Hephaestus.git && cd Hephaestus/ && echo 'TOKEN=INSERT_YOUR_TOKEN_HERE' | sudo tee -a .env && sudo docker compose -f Docker-compose.yml up -d --build"
```
Broken down by commands....

SSH into your server

```ssh -i "SSH_KEY.pem" USER@some.cloud.server.com ```

cd into the srv directory, and remove any old versions you have there.

```cd /srv/ && sudo rm -r Hephaestus ```

Clone the repo

```sudo git clone https://github.com/practical-python-org/Hephaestus.git ```

CD into the new directory, and make an env file containing your TOKEN

```cd Hephaestus/ && echo 'TOKEN=INSERT_YOUR_TOKEN_HERE' | sudo tee -a .env```

Using docker compose, rebuild any changes, and bring the bot online.

```sudo docker compose -f Docker-compose.yml up -d --build```


##### Running the bot locally
This is much simpler.

Clone the repo wherever you'd like: ```git clone https://github.com/practical-python-org/Hephaestus.git```
   
You may run the bot using ```python main.py TOKEN=YOUR-TOKEN-HERE```
OR
By setting ```TOKEN=YOUR-TOKEN-HERE``` as an env-variable. 

Hephaestus will first look at the run arg, and if there is no token, it will look at env-variables.


### Structure Overview
/Hephaestus
- Contains the Docker-compose file for the whole project, plus a gitignore.

/Hephaestus/bot
Contains the main.py, requirements, a toml, a dockerfile, and the db (when run locally)

/Hephaestus/bot/cogs
- Admin
  - contains the on_startup, which also handles connecting to the DB. 
- commands
  - any commands that a user can interact with
- database
  - contains backup commands, as well as listeners that update the db based on user events.
- logging
  - contains the bulk of the logging listeners.
- moderation
  - listeners for not-so-nice events.
- utility
  - contains helper functions for creation of the DB, all the functions that use the DB, and the embeds that are used across the whole bot.

/Hephaestus/bot/logs
- Contains the logger script, which allows you to set the logging level. Also hosts the master log file. 