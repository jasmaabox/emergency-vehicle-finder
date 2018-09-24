Prompt
  - Find EMS vehicles (given adverse conditions)?
    - US fire, police, ems vehicles

Ideas + Brainstorm
  - OpenCV using haar classifier
    - Pull positives and negatives from online -> crop square -> scale to 250px?
    - Train on Colab? AWS + GPU?
	- DON'T FORGET TO SEPARATE TEST AND TRAIN DATA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
  - data augment so we don't need to find that many images
    - convert to grayscale
    - affine transforms + gaussian noise
  - histogram equalize for bad image conditions