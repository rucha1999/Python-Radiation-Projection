# Python-Radiation-Projection

PROJECT ON DISPLAYING RADIATION-TIME GRAPH USING PYTHON - By Rucha Tirodkar
Under the guidance of Mr. Shashank Saindane (Scientific Officer, EP&R Section, Radiation Safety Systems Division, BARC)

OBJECTIVE:
Displaying and comparing graph using data of Radiation Level of 22 locations and applying advance python concepts like GUI and Database management (MySQL).

*Some crucial points to consider:
Used  python version 3.7.3 (64-bit) , Download link -https://www.python.org/downloads/

![image](https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/1c413f4f-37d4-4753-bcca-f24df37c689c)


The downloaded file runs and creates a python folder in C: drive named Python37. (This will not occur ,if we already have another version of python in PC)

To display graph used MATPLOTLIB Library and to import CSV file used PANDAS Library.

For current downloaded python file ,its necessary to import MATPLOTLIB and PANDAS library ,procedure given below – 
•	Open System properties and choose Advance system settings>System properties>Environment variables
•	In system variable value search path and select it and choose edit

<img width="599" alt="image" src="https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/7294f103-df70-49f1-9d27-744d1b34b545">

•	In Variable value: append this –
;C:\Python37;C:\Python37\Scripts
and select OK and again OK in Environment variable window to set path for command prompt.
•	OPEN command prompt and enter following command one by one :
1.	python –m pip install –U pip
2.	pip install matplotlib(takes Max 2 mins)
3.	pip install pandas(takes 2 mins)
4.	pip install tkcalender.

After successfully installing MATPLOTLIB and PANDAS we are ready to execute our python program.

STEP BY STEP PROCEDURE TO DISPLAY RADIATION GRAPH
* Download and unzip the folder named “Main project” from the mail.
* After unzipping track the “Main project” folder from downloads and move it to the python folder for a convenient access. (python folder is usually saved in C: drive named as Python37)
* Open the “Main project” folder and right click on “`RADIATION FILE” and choose edit with IDLE
* RUN the code to get the result

RESULT:
•	After running the python program, following GUI is displayed, choose the TASK  from the options.
![image](https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/bb82e4f6-1091-4182-a303-159a85f3a30a)

![image](https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/f8bc2f30-7b22-4224-a949-b3e863ba24ad)

•	Choosing INDIVIDUAL GAPH :

![image](https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/d68b577d-03ff-4eb6-a55a-d4079bdc50d6)

![image](https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/3064aa2f-2be4-489d-96ab-727cffa704b4)

![image](https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/2fee105e-ff77-4ec5-90da-9df85507fab7)

![image](https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/6d006d77-b682-4427-8f9a-52219d57edae)

•	Choosing COMPARISON GRAPH :

![image](https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/51a5cad2-ad19-4cf0-9629-76a84af7b281)

•	After selecting the time, we will  get the comparison of  radiation level graph of different specified  location at selected time frame.

![image](https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/cc0f1082-e609-4b98-9658-3d8b7cebd6e7)

![image](https://github.com/rucha1999/Python-Radiation-Projection/assets/76157534/e8f57633-e692-41b0-88a3-9441481138ee)

********************************************* Thank You  *********************************************

 
