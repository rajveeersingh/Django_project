#!bin/bash
sudo pip3 install virtualenv
## for creating virtual env
virtualenv env
source env/bin/activate
git clone https://github.com/rajveeersingh/Django_project.git

sudo apt-get update
sudo apt install python3
sudo apt install python3-pip
python -m pip install Django
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip3 install mysqlclient
pip3 install pandas
pip3 install matplotlib
pip3 install sklearn
pip3 install wordcloud
pip3 install seaborn
sudo apt-get install apache2 libapache2-mod-wsgi-py3

cd Django_project
##https://medium.com/saarthi-ai/ec2apachedjango-838e3f6014ab  for djagno+apache2 and ec2

## https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04

#mysql -h database-2.c9qzkbmyttzg.ap-south-1.rds.amazonaws.com -P 3306 -u admin -p dbda_aug_19 < project.sql
#scp -i /home/superadmin/DBDA/project/My_Project/project.pem /home/superadmin/DBDA/project/My_Project/project.sql ubuntu@65.0.80.143:~

#ssh -i /home/superadmin/DBDA/project/My_Project/project.pem ubuntu@65.0.80.143

#mysql -h database-2.c9qzkbmyttzg.ap-south-1.rds.amazonaws.com -P 3306 -u admin -p
