##### Data Structures
## About this project
Implementation of a python script that sends a JSON file to a mosquitto server running
locally via MQTT protocol. This file is sent as a string to the server.

## System Requirements
- Python 3
- paho.mqtt.client
- time
- json

## How to use
- pip install paho.mqtt.client
- python3 main.py



#### Sign List
|   Commit type              | Sign                                          |
|:---------------------------|:----------------------------------------------|
| Initial commit             | :tada: `:tada:`                               |
| New feature                | :sparkles: `:sparkles:`                       |
| Bugfix                     | :bug: `:bug:`                                 |
| Documentation              | :books: `:books:`                             |
| Documenting source code    | :bulb: `:bulb:`                               |
| Cosmetic                   | :lipstick: `:lipstick:`                       |
| Tests                      | :rotating_light: `:rotating_light:`           |
| General update             | :zap: `:zap:`                                 |
| Improve format/structure   | :art: `:art:`                                 |
| Refactor code              | :hammer: `:hammer:`                           |
| Removing code/files        | :fire: `:fire:`                               |
| Security                   | :lock: `:lock:`                               |
| Critical hotfix            | :ambulance: `:ambulance:`                     |
| Work in progress           | :construction:  `:construction:`              |
| Configuration files        | :wrench: `:wrench:`                           |
| Reverting changes          | :rewind: `:rewind:`                           |
| Merging branches           | :twisted_rightwards_arrows: `:twisted_rightwards_arrows:` |
| Bad code / need improv.    | :hankey: `:hankey:`                           |
| Code review changes        | :ok_hand: `:ok_hand:`                         |
| Move/rename repository     | :truck: `:truck:`                             |
| New feature added          | :new: `:new`                                  |
| Other                      | [Be creative](http://www.emoji-cheat-sheet.com/)  |
Standart documentation based on: [Emoji List](https://gist.github.com/parmentf/035de27d6ed1dce0b36a)

#### Control Task List
- [x] Publish json to a topic in mosquitto server
- [x] Subscribe to topic (in node-red)
- [x] Filter the topic content (in node-red)
- [x] Publish back a message to another topic into the same server
- [] Comment source code

#### TODO
- [] Try to send json instead of string to the server


#### Project Customer
This project was developed as study project. There isn't customer.

## Authors

* **Lucas Fiorini Braga** - *Computer Science student of Federal
University of Lavras* - lucasfiorini@msn.com


## License
This project is licensed under no license. Copyleft is freedom!
