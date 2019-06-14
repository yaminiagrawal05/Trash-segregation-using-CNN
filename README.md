# Idea  
 I plan to build a reward based system for waste collection and segregation.My idea is to install waste collection bins which will be having a camera and a RFID card reader installed for detection of the type of waste being put in and will reward the person with points if they deposit the waste in the correct bin.
 
# Plan of action :
 The trash will be shown to the camera at the dustbin.Image Processing and machine learning will be used to detect the type of waste
being put in the dustbin.A model will be trained to categorise the waste into biodegradable and non-biodegradable.Every person will be issued a card. The person will show his/her ID to the RFID card reader attached to the bin. A point will be issued only on the correct deposition of the waste, when the person will show his ID.➢The points can be converted into discounted products at the nearby grocery store.
 
 # Dataset
 The dataset used for this is available on github repositry of  garythung/trashnet, whuch contains the following.
501 glass
594 paper
403 cardboard
482 plastic
410 metal
137 trash
 However, after running the Convolutional Nueral Network Algorithm with a laerning rate of 0.01 , batch size as 32 and epochs = 25, the acuracy was 23%. There was need for the additional dataset and hence I am right now adding more data to the original dataset.
 
# training and testing the model
I have trained the model on a pretrained model. I have used the spyder IDE for this purpose.


# TODO's 
 This project right now is at its initial stages. I am  building a large dataset comparing to what is available right now.
Since the percentage accuracy was very less using the CNN nodel, I plan to use different ML algorithms to try and achieve greater accuraccy.
Also, for the hardware part, I am curently working on establishing the connection of RFID to generate a database through android app. I will soon be aploading the code for the same.
 
