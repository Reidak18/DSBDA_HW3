yum install -y dnf 4.2.23
sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY*
sudo yes | dnf install scl-utils
echo "INSTALL PYTHON"
dnf install python3 -y

sudo pip3 install vkstreaming

echo "INSTALL GIT"
sudo yes | dnf install git
sudo git clone https://github.com/Reidak18/DSBDA_HW3.git

echo "INSTALL JAVA"
sudo yes | dnf install java-11-openjdk-devel

echo "INSTALL ELASTICSEARCH"
sudo rpm --import https://artifacts.elastic.co/GPG-KEY-elasticsearch
sudo yes | cp DSBDA_HW3/elasticsearch/elasticsearch.repo /etc/yum.repos.d/elasticsearch.repo
sudo yes | dnf install elasticsearch
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service