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

curl -X POST http://localhost:9090/headlines \
  -H 'Content-Type: application/json' \
  -d '{
    "client_name": "aa",
    "option": 1.1,
    "country": "us",
    "category": "general"
}' &

curl -X POST http://localhost:9090/headlines \
  -H 'Content-Type: application/json' \
  -d '
  {
    "client_name": "ab",
    "option": 1.1,
    "country": "gb"
}
  ' &

curl -X POST http://localhost:9090/headlines \
  -H 'Content-Type: application/json' \
  -d '{
    "client_name": "ak",
    "option": 1.1,
    "country": "ma"
}' &

wait
