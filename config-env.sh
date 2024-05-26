#!/bin/bash

# This is a Bash script file named config-env.sh
# It is used to configure environment variables for a project or application
# Environment variables allow you to customize the behavior of programs
# without modifying the source code directly

printf "\033[1;35mConfiguring env\033[0m\n"

python3 -m venv proj_env

source proj_env/bin/activate

pip install -r requirements.txt

clear
sudo chmod 777 "scripts/*"
alias B15="./scripts/run.sh"

printf "\033[1;35mEnv Config Done!\033[0m\n"
printf "To run the server, run 'B15 server'\n"
printf "To run the client, run 'B15 client'\n"
printf "To view more info, run 'B15 info'\n"
