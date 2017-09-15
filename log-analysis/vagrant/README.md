# Project 3: Logs Analysis

This project is a Python script that executes queries against a PostgreSQL database. The script and database are both run on  Linux-based VirtualBox VM configured with Vagrant. The project specification posed three questions, which can be answered by crafting and executing queries against a database containing information about articles, their authors, and page views for each article.

## Motivation

This project is the first in a series of projects I am completing for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Getting Started

The following instructions will explain how to get a copy of this project running on your local machine.

### Prerequisites

* Python 3.x
* VirtualBox
* Vagrant

### How to Run Project

1. Install VirtualBox. You can download it from virtualbox.org [here](https://www.virtualbox.org/wiki/Downloads), or if you use [Homebrew](https://brew.sh/) you can type the following in your terminal:

    ```bash

    > brew cask install virtualbox
    ```

2. Install Vagrant. You can download it from vagrantup.com [here](https://www.vagrantup.com/downloads.html), or if you use [Homebrew](https://brew.sh/) you can type the following in your terminal:

    ```bash

    > brew cask install vagrant
    ```

3. Download or clone this repository to your machine, and navigate to the project directory:

    ```bash

    > git clone https://github.com/ewhanley/udacity-full-stack.git
    > cd udacity-full-stack/log-analysis/vagrant
    ```

4. Download the data to populate the project database [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will have to extract the file and put the `newsdata.sql` file into the `/vagran` directory from Step 3.

5. Next, start the virtual machine by typing:

    ```bash

    > vagrant up

This will install all of the required library dependencies for Python as well as hydrate the database. If you're interested in the details of this, check out `vagrant/Vagrantfile`, which is a slightly modified version of the config provided by Udacity as part of this project.

6. After the VM is up and running, log into it by typing:

    ```bash

    > vagrant ssh

7. Once you are logged into the VM, you will have a new prompt in your terminal. Navigate to the project directory:

    ```bash

    vagrant@vagrant:~$ cd /vagrant
    ```

8. Finally, run the Python script:

    ```bash

    vagrant@vagrant:/vagrant$ python3 logs_analysis.py
    ```

    or

    ```bash

    vagrant@vagrant:/vagrant$ ./logs_analysis.py
    ```

The script will output three questions and their answers in tabular format to the terminal. It will also write the same text to a file called `output.txt` in the `vagrant' directory.

**Note:** The VM is configured such that all Python dependencies are pre-installed. Additionally, the database is rebuilt each time the VM image is reloaded. If you ever need to refresh the database, you can type `exit` or `Ctrl-d` to get back to your machine's prompt where you can run:

    ```bash

    > vagrant reload
    ```

This will reload the VM from the config in Vagrantfile, which will recreate the database.