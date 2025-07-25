# generate pem file
sudo openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout brasil-test.key -out brasil-test.crt
# generate pfx file
openssl pkcs12 -export -out brasil-test.pfx -inkey brasil-test.key -in brasil-test.crt
