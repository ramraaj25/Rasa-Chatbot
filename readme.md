# Rasa Chatbot

A Rasa based Chatbot for Google Developers Student Clubs (DSC), CVRGU's official website.

## Installation

For those who want to run this project according to its requirements, please follow the steps:

#### Make a new enviroment (Recommended)
```bash
conda create -n myenv python=3.7
```
We are using python = 3.7 because rasa did not support python 3.8 when this project was developed.
#### Activate the Enviroment
```bash
conda activate <env name>
```
#### Installing Required Packages
```bash
pip install -r requirements.txt
```

#### Training the data
```bash
rasa train
```

### Running the Chatbot

#### Run the rasa action server

``` bash 
rasa run actions
```

There are two options to run the rasa based chatbot.

#### Running chatbot on command line

``` bash
rasa shell
```
#### Running chatbot with Rasa X (Interactive learning)

This is the most preferable way of running the chatbot of Rasa. Run below commands to run the chatbot in interactive way.
 ```bash
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```
After installation,
```bash
rasa x
```
Now you can see the chatbot running in interactive mode.
