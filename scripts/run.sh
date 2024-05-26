#!/bin/bash

 
# This script is used to run different components of the 
# application


# Usage:
#   ./run.sh [option]

# Options:
#   server   Start the server component
#   client   Start the client component
#   info     Display the project README file

# The script first checks the provided argument and performs the corresponding action.

# If 'server' is passed, it navigates to the '../server' directory and runs the 'server.py' script.
# If 'client' is passed, it navigates to the '../client' directory and runs the 'client.py' script.
# If 'info' is passed, it navigates to the root directory and displays the 'README.md' file using the 
# 'rich.markdown' module.

# After executing the respective action, the script exits.

if [ $1 == "server" ]; then
  ./scripts/server.sh
elif [ $1 == "client" ]; then
  ./scripts/client.sh
elif [ $1 == "info" ]; then
  python -m rich.markdown README.md
else
  echo "Invalid argument. Use 'server', 'client', or 'info'."
fi
