## Superhero API
![Titlecard displaying some superheroes](https://imgur.com/Sd8iZkH)
### Contributors:

- [Dylan Peterson](https://github.com/DyPeterson)

### Description

A [Data Stack Academy](https://www.datastack.academy/) code review project to work with APIs. Make an API that allows the GET and POST methods.
  

### Technologies Used:

- [Python](https://www.python.org/)

- [Pandas](https://pandas.pydata.org/)

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
#### Programs used:
- [Visual Code Studio](https://code.visualstudio.com/)
- [Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=US) ( Running: [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install) ([ubuntu 20.04](https://releases.ubuntu.com/20.04/)))
- [Postman](https://www.postman.com/)
- [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)
### Setup & Installation:

1. Through the terminal like [GitBash](https://git-scm.com/downloads)

  
	
	1. Open the terminal and navigate to where you would like the new project to be using `cd` commands. Its also recommended that you make a new directory using `mkdir *directory-name*`.

	  

	1. Clone the repository using the command `git clone https://github.com/DyPeterson/api_cr`

	  

	1. After cloning the directory it will appear in the directory that your terminal is set to. So make sure you are in the directory that you want this project copied to.

	  

	1. Once this project is cloned you can navigate to that folder within your terminal and create a virtual environment `python3.7 -m venv *any-name*`. Now activate the venv with `source *any-name*/bin/activate`

	  

	1. Install requirements in venv `pip install -r requirements.txt`

	  

	1. Download the data by running the `get_data.sh` either by clicking it or running in the terminal.

	  

	1.  `code .` to open in default coding software.

  

2. Through GitHub.com

  
	
	1. Go to the project's directory page **[HERE](https://github.com/DyPeterson/api_cr)**

	  

	2. Click the green `code` button to open the drop-down menu.

	  

	3. At the bottom of the menu will have *Download Zip*. Go ahead and click it to download the project.

	  

	4. Once downloaded find the `.zip` file and right-click it to bring up the menu. Within that menu click `Extract Here` to extract it in the current folder or click `Extract Files...`to select which folder you would like the project in.

	  

	5. Once the project has been extracted, locate the folder in a terminal and open it with `code .` .
	
	7. Run the `main.py`  with the command `python main.py`to run the API locally

### Working with the API
I used Postman to work with the API, but other tools exist so feel free to use your own, but this tutorial is Postman focused.
#### GET Method:
This method allows you to query the data to search for superheroes.
Set the endpoint to `/see_stats` and make sure the GET is selected in Postman, you can also use a web browser to use this method(more on this later).
Now select the "params" tab below that. Now we can start querying the database.
To do this you **must** set the key to atleast one of the following (you can also select more than one for a more specific search):

 - `name`
 - `superpower`
 - `weakness`

Now it the value field type what you would like to query the database for, currently there is only 3 default heroes, but you can add more with the POST method(below)
Once you have a query inserted to can press the `SEND` button to query. This will return a superhero if one in the database matches your query.

##### Using the web browser:

To use the web browser you can manually type out your query in the address bar.
first make sure you web browser is set to the end point: `<ip.address.is.here>:5050/see_stats`. Next add a question mark followed by the key you are searching through followed by an equals sign and the query for that key.
For example: `<ip.address.is.here>:5050/see_stats?superpower=Radiation`

#### POST Method:
To add superheroes to the database you need to use the POST method detailed below:
Set the endpoint to `/add_stats`, make sure that POST is selected from the drop-down menu. Then select `Body` below that, on the next line below that select `raw` and also `JSON` from the drop-down menu.
From here we are ready to start adding superheroes to our database.
To do so, we need to follow a specific syntax and include all three keys of our database,`name`,`superpower`&`weakness`. The values you type in for the keys will be what gets added to the database. After that press the `SEND` button and viola! Here's an example of what this looks like, followed by a picture of what it looks like in the Postman app
```
[
	{
		"name":  "The Rock",
		"superpower":  "Peoples Elbow",
		"weakness":  "Insecure about cooking"
	}
]
```

![Image of Postman program highlighting the dropdown menu with POST selected.](https://imgur.com/B58kAXr)
```
[
	{
		"name":  "The Rock",
		"superpower":  "Peoples Elbow",
		"weakness":  "Insecure about cooking"
	}
]
```
#### Link to project on GitHub:
[GitHub Repository](https://github.com/DyPeterson/bigquery_cr)

### Details
This project uses Flask to create an API that hosts a database of superheroes. The superhero attributes are `name` ,`superpower`&`weakness`. It allows the user to query(GET) and add(POST) heroes to the database.


Contact me with any questions or suggestions [Here](dylan.peterson17@gmail.com)

  

### Known Bugs

 No known bugs at this time.

  

### Copyright 2022

  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

  

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

  

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.