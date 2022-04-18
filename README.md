# vk_sheety_posts

  this bot allows you to compleete some kind of subscription mechanics with preliminary (text) content.

it sends messages in 8.30am to all selected followers three times per week (wednesday, thursday, friday)


## Setup
Install the requremets and configure the CRON table: <br>
  `cd <PATH_TO_PROJET_DIR>` <br>
  `make setup`

to test the script in action enter:<br>
  `make start`

to disable script:<br>
  `make stop`
 
## Setting configuration
  to make the bot work properly replace the following lines in `config.json` file:<br>
  * peers_id : [<br>
        `<YOUR SUBSCRIBER CHAT ID #1>` ,<br>
        `<YOUR SUBSCRIBER CHAT ID #2>` ,<br>
        `...`<br>
  ]

  
  to insert telegram bot key:
  * make file `token.txt` and put your bot token into this file

## Example of program execution
