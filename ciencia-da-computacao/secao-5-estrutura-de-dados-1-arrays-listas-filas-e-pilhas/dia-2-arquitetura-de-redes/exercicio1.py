# Faça uma chamada GET, utilizando o cURL.
"""curl localhost:3000
ou
curl -X GET localhost:3000"""

# Faça uma chamada POST, utilizando o cURL, passando um JSON no body da
# requisição.
"""curl -X POST \
    -H 'Content-Type: application/json' \
    -d '{ "foo": "bar" }' \
    localhost:3000"""

# Faça uma chamada qualquer, utilizando o cURL, passando um header na
# requisição.
"""curl --request POST \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Apikey EXAMPLE-TOKEN' \
    --data '{ "foo": "bar" }' \
    localhost:3000"""
