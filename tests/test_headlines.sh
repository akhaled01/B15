printf "\033[1;32mTESTING HEADLINES\033[0m\n"

curl -X POST http://localhost:9090/conn \
  -H 'Content-Type: application/json' \
  -d '{"client_name":"ak"}'
echo "\n"


curl -X POST http://localhost:9090/headlines \
  -H 'Content-Type: application/json' \
  -d '{"client_name": "ak","option": 1.1,"country": "us","category": "general"}'
echo "\n"

curl -X POST http://localhost:9090/disconn \
  -H 'Content-Type: application/json' \
  -d '{"client_name":"ak"}'