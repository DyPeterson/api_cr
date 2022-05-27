
## Superhero API
![Titlecard displaying some superheroes](https://lh3.googleusercontent.com/A1ak5JQm_BH94QKENei3EgZ0S1qywANQIKW7HseyRYSczo3QW848D1cHYKbo9gQdj5WmqrR56ALT0KRk4gvaChLVLKfiRL6hCbg6vMr0lfWrFbD4PpvD6798RtnPOGeAlUvkwAIXAqf3m9GO2EFBkNoN37VcBeKYJg3hPD-hWvv3axRc9mT8jr8IojzCUtei0mX1v4CPAgtnLo_u5Rzfh68qSEyugiVX-mWU81NhmFlsC85C9bVs_VnXyq_UTBEQR_hqafsh-WWdMptdBlQHuudXC9jzjBtEdqwvctG7MIdBH4tAdGbpXr_UfIsTF-h-U9oz4lEVXpeZhbIsPcfk0tDahGV7IqlhDhY1JYUZipXd15_S8XhdEYu5AV4ap5R8Mmb6xhZezdPKHv-ZY5Xqk1jv8ow-9qfRmuVNaUeXpcMov9GkWnIg9cMI-o8priL0Hxu4Pf3L5eQS8QSOdB4m7hf6w3uIAra89pYiwlqKn5c3YSCcH-TpBzZnLjMekXP_sjRZF-o1yiVskXO2sal4w3ppsZiFAjTF7loGYpehRx0EUdbS0xmUUUJRx1SKC2imYD4hA5Yg4vZZNlPB1VpuIVfKLAisZnRDoGobonUmkHv_ZkUSsDb2uMJWXPc4ZWJTVMpkeOZHb0TQhB6OS86a4O2-XqzBoBLw3ZiJ7uFDyDU19DwArT-uXeKjsiVvMNbA2CwxQc2VoEiEZB2U9PtWrr1U52jSyvNnDMYjS5BFK65aeBxPc-IJDLK-Hgoh3P-Ubkq5lovjPoEeMuaQO10Jo66P6o8RGMU-peU=w640-h320-no?authuser=0)
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
Set the endpoint to `/see_stats`
#### POST Method:
Set the endpoint to `/add_stats`
![Image of Postman program highlighting the dropdown menu with POST selected.](https://lh3.googleusercontent.com/LFcmF5nvS_fd1neeBRC9Ti3lYnnrp5iQxH7QTt2zX9j-virO1E339KDdSquY4s63rEu-driQSCQE-bWK32lE-QQGpzLlcTbWZ3pBniHNLDNFIBD_3CvdwVJv0wrZyWIP0oUMSLBKNTurowmSwRQ_tBw-zRx2WdFiW8KkpbV_mgpSQOqL8ON7ANYtjTOPAmhbVf2DPjYp4ZI2mKAPccs2nfjf2M7DK3SlJDTl321fEAhk5r-N81BEw_bwIZ6nUlhJuu-oBZf9ocglEy5e5HgPnNDjeelHhQlRg5VMpluEogiLMWCJZ2tE0RHQbSpgKTjcNS2uHth2nPwmGXRYo2upg0UsTcGBHEGkHX0Fw8FaODeIz1xzWUhDY983GnBZMpawDuFMlLTKsCmHgUB2rtRlq_RPt7QFjBnWNtxSQ9sU2pJjzOnRkQG_wi8C_tAHmlCKQqTDmFhP0lwj9v8ygDJ1GA0X1ke6Q7iTu4seoZXx7rIAbwU9dSebTyXe_dYgMWryE7GK0QbjIOhbiAuSzg5ew4wxIsW2in3ZLnwNmSlQDAAI_7b_HeMHTcg4CJuUYvIc5fHXP7OfJu98zrzvLcqbdNcDFl3c_L2kFABLPslo-LTe_ocvpS0Uv2E_UogDl4cIuYfTpttJfBpyco7xPhHnKBE-Yd_6LNywBEv_aBifQl3zbqY-sJ5VwGB8hkQ71Vk0Y460pULjO0xo5YJNJNiBE8nlQL4CrqBaL1BC6oubg2kqH7avxV9UYScL9v0_q_6Scst-C-y7yJuh_hFl-dyFItj86BaU4x_Vwjc=w1017-h684-no?authuser=0)
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