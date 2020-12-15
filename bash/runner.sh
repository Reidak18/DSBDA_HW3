sudo apt install virtualbox 
wget https://releases.hashicorp.com/vagrant/2.2.14/vagrant_2.2.14_x86_64.deb
dpkg -i vagrant_2.2.14_x86_64.deb
rm -f vagrant_2.2.14_x86_64.deb
vagrant plugin install vagrant-vbguest
vagrant plugin install vagrant-scp

# Запуск виртуалки
vagrant init centos/7
vagrant up

# Копируем запускаем скрипт на виртуалку
vagrant scp script.sh default:/home/vagrant 

# Запускаем скрипт
vagrant ssh -- 'sudo sh script.sh'
vagrant ssh
