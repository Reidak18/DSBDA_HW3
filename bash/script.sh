sudo su
yum install -y dnf 4.2.23
sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY*
sudo yes | dnf install scl-utils
echo "INSTALL PYTHON"
sudo yes | dnf install python3
sudo yes | pip3 install vkstreaming

echo "INSTALL GIT"
sudo yes | dnf install git
sudo git clone https://github.com/Reidak18/DSBDA_HW3.git

echo "INSTALL JAVA"
sudo yes | dnf install java-11-openjdk-devel

echo "INSTALL ELASTICSEARCH"
sudo yes | dnf install wget
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.9.3-x86_64.rpm -P elastic
sudo dnf -y localinstall elastic/elasticsearch-7.9.3-x86_64.rpm
sudo systemctl enable elasticsearch.service
sudo systemctl start elasticsearch.service