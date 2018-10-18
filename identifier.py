import os
import cv2

SHOW_VIDEO = True

# load classifiers
firetruck_haar = cv2.CascadeClassifier('data/firetruck_cascade_5.xml')
ems_haar = cv2.CascadeClassifier('data/ambulance_cascade.xml')
police_haar = cv2.CascadeClassifier('data/police_cascade.xml')

def find_center(x):
    """Finds center of roi"""
    return [int(x[0]+x[2]/2), int(x[1]+x[3]/2)]


def process_img(img):
    """Returns array of locations of emergency vehicles"""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # ADD OTHER CLASSIFIERS

    firetrucks = firetruck_haar.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=20)
    ems = ems_haar.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=40)
    police = police_haar.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=20)

    # show vid
    if SHOW_VIDEO:
        for (x, y, w, h) in firetrucks:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
        for (x, y, w, h) in ems:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        for (x, y, w, h) in police:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
        cv2.imshow('frame', img)
        cv2.waitKey(1)

    emergency_vehicles = []
    emergency_vehicles += list(map(find_center, firetrucks))
    emergency_vehicles += list(map(find_center, ems))
    emergency_vehicles += list(map(find_center, police))
    
    return emergency_vehicles


def main():
    # load files
    with open('in2.txt', 'r') as f:
        fpaths = f.read().split('\n')

    # process data
    for f in fpaths:
        
        if f[-3:].lower() == 'bmp':
            img = cv2.imread(f)
            res = process_img(img)

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
                
                res = process_img(frame)
                loc_arr.append(res)
                num_arr.append(len(res))
                
            print('\n'.join([str(num_arr), str(loc_arr)]))

        print()


if __name__ == '__main__':
    main()
        
