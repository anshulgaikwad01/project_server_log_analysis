# Server-Log-Analysis (Udacity-nd project 2)

An internal reporting tool that uses information of large database of a web server and draw business conclusions from that information. (Project from Full Stack Web Development Nanodegree)

## Introduction


This is a python module that tries to ascertain the usage of web services using the information of large database of a web server, and helps in drawing important insights from that Information. The database is consisted of three tables, that is: 

+ The __authors__ table includes information about the author of articles.
+ The __articles__ table includes the articles themselves.
+ The __log__ table includes entries of all the client requests and server response in the form of _status code_.

### The project drives following conclusions:

+ Most popular three articles of all time.
+ Most popular article authors of all time.
+ Days on which more than 1% of requests lead to errors.

## Instructions

+ __Install [Vagrant](https://vagrantup.com/downloads.html) and [Virtualbox](https://www.virtualbox.org/wiki/Downloads).__

+ __Clone the repository to the local machine__  

+ __Start the virtual machine__

From your terminal, inside the project directory, run the command `vagrant up`. This will cause Vagrant to download the Linux operating system and install it. When vagrant up is finished running, you will get your shell prompt back. At this point, you can run `vagrant ssh` to log in to your newly installed Linux VM!


+ __Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).__

You will need to unzip this file after downloading it. The file inside is called _newsdata.sql_. Put this file into the vagrant directory, which is shared with your virtual machine.


+ __Setup Database__

To load the database use the following command:

`psql -d news -f newsdata.sql`

+ __Run Module__

`python3 main.py`