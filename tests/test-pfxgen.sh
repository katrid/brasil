# generate pem file
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout test.key -out test.crt -subj "/C=US/ST=SP/L=Sao Paulo/O=My Company/OU=IT Department/CN=example.com"
# generate pfx file
openssl pkcs12 -export -out test.pfx -inkey test.key -in test.crt -passout pass:12345678
