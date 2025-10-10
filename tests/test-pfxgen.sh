# generate pem file
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout test.key -out test.crt
# generate pfx file
openssl pkcs12 -export -out test.pfx -inkey test.key -in test.crt
