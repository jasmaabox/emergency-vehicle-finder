# Data

Notes on classifiers

### Firetrucks
  - firetruck_cascade
    - 33 stages
	- trained from Google Image firetrucks against random images
	- bad performance and low positive count
  - firetruck_cascade_3
    - 35 stages
	- trained from ImageNet firetrucks against random images
  - firetruck_cascade_5
    - 30 stages
	- trained from ImageNet firetrucks and Google Image firetrucks against random images

### Ambulance
  - ambulance_cascade
    - 25 stages
	- ImageNet ambulances trained against ImageNet streets

### Police
  - police_cascade
    - 32 stages
	- trained from ~500 positive police cars from ImageNet against street images
  - police_cascade_2
    - 30 stages
	- trained from 800 positive images from ImageNet and Google Images against street images