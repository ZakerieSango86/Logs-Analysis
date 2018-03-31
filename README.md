## Logs-Analysis


### Installation 
The code contained in this repository requires installation of: 
- Virtualbox
- Vagrant 

As the installation instructions are originally provided by Udacity, I have not replicated them here. 

### Executing the code 

Once the above applications are installed: 

1. Clone this repository to a local folder, using git clone 
2. Initialise the linux virtual machine by opening the /Vagrant folder from your command line and entering 'Vagrant SSH' 
3. Once inside the VM, `$cd` to `\vagrant\News` 
4. Execute the news python file using `python news.py`. This will create a html file in the same directory 
5. From the same directory open the html file using `open news.html`

### Notes about the code 

The code is brittle, I'm not quite at the level of coding quality yet to completely abstract the query complexity away from the presentation of the results in the html. As such, a number of the python modules are dedicated to the retrieval, formatting and presentation of a specific SQL query. 


