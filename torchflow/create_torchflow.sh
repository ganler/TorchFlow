set -e

MAINDB="torchflow"
DBUSER="torchflow"
PASSWD="TorchFlow@Jiawei233"

echo "[[TorchFlow > Please enter root user MySQL password!"
echo "[[TorchFlow > Note: password will be hidden when typing."
read -sp "[[TorchFlow > [ENTER THE PASSWD]:::" rootpasswd

MYSQL_PWD=${rootpasswd} mysql -uroot -e "create database if not exists ${MAINDB}; source $(dirname "$0")/init.sql;"
MYSQL_PWD=${rootpasswd} mysql -uroot -e "use ${MAINDB}; show tables;"

MYSQL_PWD=${rootpasswd} mysql -uroot -e "create user if not exists '${DBUSER}'@'localhost' identified BY '${PASSWD}';"
MYSQL_PWD=${rootpasswd} mysql -uroot -e "grant all privileges on ${MAINDB}.* to '${DBUSER}'@'localhost';"
MYSQL_PWD=${rootpasswd} mysql -uroot -e "flush privileges;"
MYSQL_PWD=${rootpasswd} mysql -uroot -e "SHOW GRANTS for '${DBUSER}'@'localhost'";