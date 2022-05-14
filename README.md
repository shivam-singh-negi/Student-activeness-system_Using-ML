# Student-activeness-system_Using-ML
In this system the student will be asked certain number of questions during an session(online class maybe) at any random time . The student can either miss , attempt the question within a time frame after that the question window will clossed. Along with this the system will capture details like no of scrolls ,clicks and mouse movements that took place  during the entriire session and during the questions window pop up. At the end of the session the data like right , wrong, missed questions, accuracy of answering right, mouse clicks , scroll and user_id  will be send to a centralised server. The server will accumulate the same data from multiple user . This will built up the dataset. On the dataset formed we will implement Machine learning algorithms like SVM and KNN to train the system to classify the userid into categories like "very Active", "active", "Less Active" and "Least active".
The files-
--------------------------------------------------------------------------------------------------------------------------
main.py -it is a web scrapper made to extract mcqs from the website sanfoundry.com for pop of questions .
scratch_1.txt- it contanins links to the webpage containg mcqs on various subject for pop up purpose.
final2.csv - it contains the mcqs that are used in this project for pop up purpose.
scratch_7.py- It is the main final script that will run on the client side. And It will send the final computational data to the server.
server.py- It is the centralised system that will store the data coming from the various clients on a common file(csv).
dataset.csv- it is the common file in which the server stores the incoming data and this file will form the final dataset for training the modle and test it.
mouse_log12.csv- it is storing the data generating form the actions of mouse . it contains number of scrolls, clciks and movement during the entire seesion for 1 client. along with time stamp.
scratch_8.py- it contains the countdown timer function.
minor_project1 (2).csv - It contains the collab file used to create the dataset to train the model.
Final_dataset.csv- it is the final dataset that will be used for taining and testing.
minor activeness file1.ipynb- It is the collab file in which we have trained and tested our model using ML' algos.
