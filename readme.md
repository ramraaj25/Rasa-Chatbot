# Rasa Chatbot

Made an Rasa-Based Chatbot for Developers Student Clubs (DSC) of Cv Raman College Of Engineering.

## Installation

For those who want to run this project according to its requirements, please follow the steps:

#### Make a new enviroment (Recommended)
```bash
conda create -n myenv python=3.6
```
We are using python = 3.6 because rasa doesn't support python 3.8/3.7 perfectly when this project is developed.
#### Activate the Enviroment
```bash
conda activate myenv
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
Then, after installing the interacting mode
```bash
rasa x
```
Now you can see the chatbot running in interactive mode.
