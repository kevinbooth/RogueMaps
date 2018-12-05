**RogueMaps: Google Maps Directions Parser**

**Kevin Booth and Adam Harney**

COMP 525 Data Structures Fundamentals, Fall 2018

**Objectives  - What does the program do?**

**_Author: Kevin Booth_**



1.  Provide a way for a traveler to request a document of directions from one location to another
1.  Allow the traveler to choose their mode of transportation such as driving, walking, bicycling, or transit
1.  Save and open the document of directions locally on the traveler's computer for reference or printing
1.  Provide explicit step-by-step, street directions within the document that show estimated travel time and incremental mileage per direction step

**Design - How is the program structured? How does the data flow?**

_Use a component-based approach to describing the program's design. Divide the design in two parts (see below). **Add author name. **_

**<span style="text-decoration:underline;">Design Components_ Author: Adam Harney_</span>**



When the user executes the program, the command prompt will greet them then ask for a starting point for the directions. The entire process is generally managed by the "main.py" module. It will first import all methods from the other modules, then it will call "welcome_message" in the "user.py" module.    The module in charge of this initial interaction is "user.py." It's primary class is called "UserInterface", and the method that prints the initial greeting is called "welcome_message."  

Back in main.py, the program calls the "retrieve_user_data" method to prompt the user for the travel information surrounding the navigation.  I said method, while no arguments are taken, all input is put into a dictionary that will later be returned.  In order, the method asks the user for the starting point of the navigation, the ending point of the navigation, what mode of transportation they would like to use, and finally whether or not they would like to automatically open the document upon its generation. All input values are stored as strings. Once all the information is gathered up and put neatly into a dictionary, it is then returned into a variable in main.py called "user_data." That variable will then be sent to the method called "api_call" in the class "GoogleMapsHelper", with in the "api.py" module.  

With the dictionary as an argument api_call will send the user information to the Google Maps API and then place the results in a returnable JSON object called "directions_results." After a quick user error check, the method then returns said JSON. The main.py module first puts the data from the api.py module into a variable called "api_call_data."  Then it tests for any errors made by the user, reported by the api. If no error is found, it sends the previously stored api data to the "massage_api_response" method.

Also in the api.py module, the method called "massage_api_response" takes the JSON returned from google maps, and sorts it carefully into a dictionary.  The returned dictionary is then stored in a variable of the main.py module called "massaged_data." That dictionary variable is then passed as an argument in the "create_pdf" method.

Within the module called "document.py" and the class called "DocumentCreator", is the method called "create_pdf."  This method takes the dictionary from the massage data method and prints all pertinent information onto a pdf in an easy to read format.  Although this method does not return the file itself, it does return the path to said file so that the user can then decide if they would like to open it immediately or not.  After creating the document, the file path is returned to the main.py module as a string, which in turn is stored as a string called "full_file_path."  Finally, on the final line of main.py, the program checks for the user input regarding whether or not to automatically print the method. If the user affirms their desire to auto open the document the main class  calls the method called "open_document" sending the file path as an argument.  If the user has declined the offer to open the document, then the program will simply inform them on where they can find it.  The "open_document" method, stored within the document.py module, and the "DocumentCreator" class, simply opens the the document using the file path sent to it as an argument. The program terminates after either case.

**<span style="text-decoration:underline;">Function Diagram and Data Flow</span> _Author: Kevin Booth_**

Note: All dotted arrows represent calls to Python packages



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/project-report0.png). Store image on your image server and adjust path/filename if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/project-report0.png "image_tooltip")


**Testing**

**<span style="text-decoration:underline;">Test Cases</span> _Author: Kevin Booth_**

**retrieve_user_data**() <-- No parameters

Returns {'start_address': '1 S Main St, Manchester NH 03102

', 'end_address': '175 Canal St, Manchester NH 03101', 'travel_mode': 'driving', 'depart_now': 'y'}

**api_call**({'start_address': '1 Main St, Manchester NH 03103

', 'end_address': '175 Canal St, Manchester NH 03101', 'travel_mode': 'driving', 'depart_now': 'y'})

Returns a JSON Object seen below:

[

  {

	"bounds": {

  	"northeast": {

    	"lat": 42.9876521,

    	"lng": -71.4660095

  	},

  	"southwest": {

    	"lat": 42.9836195,

    	"lng": -71.473948

  	}

	},

	"copyrights": "Map data \\u00a92018 Google",

	"legs": [

  	{

    	"distance": {

      	"text": "0.5 mi",

      	"value": 850

    	},

    	"duration": {

      	"text": "4 mins",

      	"value": 210

    	},

    	"duration_in_traffic": {

      	"text": "3 mins",

      	"value": 206

    	},

    	"end_address": "175 Canal St, Manchester, NH 03101, USA",

    	"end_location": {

      	"lat": 42.9876521,

      	"lng": -71.4664671

    	},

    	"start_address": "1 S Main St, Manchester, NH 03102, USA",

    	"start_location": {

      	"lat": 42.9836275,

      	"lng": -71.473948

    	},

    	"steps": [

      	{

        	"distance": {

          	"text": "0.4 mi",

          	"value": 714

        	},

        	"duration": {

          	"text": "3 mins",

          	"value": 171

        	},

        	"end_location": {

          	"lat": 42.9865526,

          	"lng": -71.466161

        	},

        	"html_instructions": "Head <b>east</b> on <b>Granite St</b> toward <b>Main St</b>",

        	"polyline": {

          	"points": "ufjeGdwfsL@SEUGUI]M_@Wy@m@mBWw@Sq@cAkDCKGWAEAEQs@Qs@Qo@_BwFk@kBKa@_@mAKc@k@uBIYUcAMi@I["

        	},

        	"start_location": {

          	"lat": 42.9836275,

          	"lng": -71.473948

        	},

        	"travel_mode": "DRIVING"

      	},

      	{

        	"distance": {

          	"text": "446 ft",

          	"value": 136

        	},

        	"duration": {

          	"text": "1 min",

          	"value": 39

        	},

        	"end_location": {

          	"lat": 42.9876521,

          	"lng": -71.4664671

        	},

        	"html_instructions": "Turn <b>left</b> onto <b>Canal St</b><div style=\"font-size:0.9em\">Destination will be on the right</div>",

        	"maneuver": "turn-left",

        	"polyline": {

          	"points": "}xjeGnfesLI]WHYL[Ju@Tm@R_@L"

        	},

        	"start_location": {

          	"lat": 42.9865526,

          	"lng": -71.466161

        	},

        	"travel_mode": "DRIVING"

      	}

    	],

    	"traffic_speed_entry": [],

    	"via_waypoint": []

  	}

	],

	"overview_polyline": {

  	"points": "ufjeGdwfsL@SEUQs@kB_GcBaGg@sBiDuLk@qBu@oCw@gDcCx@mA`@"

	},

	"summary": "Granite St",

	"warnings": [],

	"waypoint_order": []

  }

]

**massage_api_response**({THE JSON OBJECT ABOVE})

Returns a dictionary of strings and lists

{

'start_address': '175 Canal St, Manchester, NH 03101, USA',

'end_address': '1 S Main St, Manchester, NH 03102, USA',

'distance': '0.5 mi',

'duration': '4 mins',

'duration_in_traffic': '3 mins',

'travel_mode': 'Driving',

'instructions': ['Head east on Granite St toward Main St for 446 ft', 'Turn left onto Canal St Destination will be on the right' ],

'step_distance': []

}

**create_pdf**({

'start_address': '175 Canal St, Manchester, NH 03101, USA',

'end_address': '1 S Main St, Manchester, NH 03102, USA',

'distance': '0.5 mi',

'duration': '4 mins',

'duration_in_traffic': '3 mins',

'travel_mode': 'Driving',

'instructions': ['Head east on Granite St toward Main St for 446 ft', 'Turn left onto Canal St Destination will be on the right']

})

Returns the full_file_path

'/home/kevin/desktop/directions2018_12_3.pdf'

**open_document**('/home/kevin/desktop/directions2018_12_3.pdf')

Returns null

**<span style="text-decoration:underline;">Program Running Instructions_ Author: Adam Harney_</span>**



	The single bash command to run the program is "python main.py" ("python3" depending on your set up).  

The program will immediately greet the user and ask for the starting point. The user enters a starting point to the best of their ability. The program will then ask for the ending point (or destination), which the user again answers to the best of their ability.  Program then asks the user whether they would like to "depart now", which is simply asking whether the user would like to automatically open the file when finished.  The input in regards to the starting and ending address is allowed user error within reason due to the intelligent error correction by the API.

**Implementation**

**GitHub Repository Name:** RogueMaps

**GitHub URL:** [https://github.com/kevinbooth/RogueMaps/](https://github.com/kevinbooth/RogueMaps/)

**Modules:**



*   Main - Performs as the central hub where all methods are executed for RogueMaps.
*   User - Provides all the methods necessary for the user interface and the retrieval of user data.
*   API - Provides custom methods that help aid in making Google Maps API calls while using the data retrieved from the User module.
*   Document - Creates different forms of document output types (only PDF is implemented) with the data retrieved from the API module.

**Evaluation**

**<span style="text-decoration:underline;">What Works and Scope Assumptions</span> _Author: Kevin Booth_**

**General Functionality**



1.  The user is able to input their starting and ending address.
1.  There are four options of travel provided to the user to choose from: walking, bicycling, transit, and driving.
1.  The user can choose whether or not they are departing now.
1.  A PDF document with step-by-step directions and estimated travel times is created and saved to the user's desktop with the following format: "directions2018_12_04.pdf".
1.  The document automatically opens for the user to see if they accept the departing now option.

**Technical Functionality**



*   Through the googlemaps Python package, we are able to query the Google Maps API with parameters containing information about a user's travel information.
*   We are parsing through the JSON object returned from Google Maps and appending it to our own object along with stripping out HTML tags with the BeautifulSoup package.
*   Using the FPDF package, we are creating a PDF file and writing our retrieved data to the file.

**Assumptions**



*   We assumed there were no HTML tags in the return JSON object from the Google Maps API but later found out that there were. This required us to incorporate the BeautifulSoup package to strip the tags out.
*   Initially, we decided to return a dictionary of lists in the massage_api_response method, but later we found out that Python doesn't natively support that ability without the import of a package. We used defaultdict from the collections package to allow the ability to append to a list at a specific key in a dictionary.
*   We were going to provide error handling on all input fields, but we found that the API provides very sophisticated street address interpretation. This allowed us to not have to check the validity of inputted addresses from the user.
*   We didn't think through being able to save a document to the desktop until that issue arose. The issue was dynamically creating the file path with the user's computer username. After some research, the os Python package gave us access to create that path.

**<span style="text-decoration:underline;">Further Development_ Author: Adam Harney_</span>**



*   Add a relevant map or maps to the side of the page for offline reference.
*   Automatic printing
*   Different text document types such as .docx or .rtf
*   The ability to choose where to save the directions file
*   Alternate routes
*   Emailing the directions to oneself or another person
*   Better, more extensive error handling
*   A file name checker to avoid overwriting past navigations
*   Multiple destinations/Pit Stops
    *   Route from both A to C as well as A to B to C
