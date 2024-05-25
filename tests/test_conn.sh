# Test client connection

printf "\033[1;32mTESTING CONN\033[0m\n"

curl -X POST http://localhost:9090/conn \
  -H 'Content-Type: application/json' \
  -d '{"client_name":"ak"}'
echo "\n"

curl -X POST http://localhost:9090/conn \
  -H 'Content-Type: application/json' \
  -d '{"client_name":"aa"}'
echo "\n"

curl -X POST http://localhost:9090/conn \
  -H 'Content-Type: application/json' \
  -d '{"client_name":"ab"}'
echo "\n"

sleep 1.4

# Test client disconnection
printf "\033[1;32mTESTING DISCONN\033[0m\n"

curl -X POST http://localhost:9090/disconn \
  -H 'Content-Type: application/json' \
  -d '{"client_name":"ak"}'

echo "\n"

curl -X POST http://localhost:9090/disconn \
  -H 'Content-Type: application/json' \
  -d '{"client_name":"aa"}'
echo "\n"

curl -X POST http://localhost:9090/disconn \
  -H 'Content-Type: application/json' \
  -d '{"client_name":"ab"}
  '
echo "\n"
