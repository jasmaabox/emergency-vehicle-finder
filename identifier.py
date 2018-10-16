import os
import cv2

def process_img(img):
    """Returns array of locations of emergency vehicles"""
    # ADD OTHER CLASSIFIERS

    firetrucks = firetruck_haar.detectMultiScale(img, scaleFactor=1.2, minNeighbors=5)

    emergency_vehicles = firetrucks
    emergency_vehicles = list(map(lambda x: [x[0], x[1]], emergency_vehicles))

    return emergency_vehicles


# load classifiers
firetruck_haar = cv2.CascadeClassifier('data/firetruck_cascade_5.xml')

def main():
    # load files
    with open('in.txt', 'r') as f:
        fpaths = f.read().split('\n')

    # process data
    for f in fpaths:
        
        if f[-3:].lower() == 'bmp':
            img = cv2.imread(f)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            res = process_img(gray)

            print('\n'.join([str(len(res)), str(res)]))
            
        elif f[-3:] == 'mp4':
            num_arr = []
            loc_arr = []
            cap = cv2.VideoCapture(f)
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    cap.release()
                    break
                
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                res = process_img(gray)
                loc_arr.append(res)
                num_arr.append(len(res))
                
            print('\n'.join([str(num_arr), str(loc_arr)]))

        print()


if __name__ == '__main__':
    main()
