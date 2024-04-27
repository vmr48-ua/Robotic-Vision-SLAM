import numpy as np
import cv2
import os,sys
from triangulation import triangulate
from Camera import denormalize, Camera
from display import Display
from match_frames import generate_match
from descriptor import Descriptor, Point

F= int(os.getenv("F","500"))
W, H = 1920//2, 1080//2
K = np.array([[F,0,W//2],[0,F,H//2],[0,0,1]])
desc_dict = Descriptor()
desc_dict.create_viewer()
disp = Display(W, H)

def calibrate(image):
    image = cv2.resize(image, (W,H))
    return image

def generate_SLAM(image):
    image = calibrate(image)
    frame = Camera(desc_dict, image, K)
    if frame.id == 0:
        return
    frame1 = desc_dict.frames[-1]
    frame2 = desc_dict.frames[-2]

    x1,x2,Id = generate_match(frame1,frame2)
    frame1.pose = np.dot(Id,frame2.pose)
    for i,idx in enumerate(x2):
        if frame2.pts[idx] is not None:
            frame2.pts[idx].add_observation(frame1,x1[i])
    # homogeneous 3-D coords
    pts4d = triangulate(frame1.pose, frame2.pose, frame1.key_pts[x1], frame2.key_pts[x2])
    pts4d /= pts4d[:, 3:]
    unmatched_points = np.array([frame1.pts[i] is None for i in x1])
    print("Adding:  %d points" % np.sum(unmatched_points))
    good_pts4d = (np.abs(pts4d[:, 3]) > 0.005) & (pts4d[:, 2] > 0) & unmatched_points

    for i,p in enumerate(pts4d):
        if not good_pts4d[i]:
          continue
        pt = Point(desc_dict, p)
        pt.add_observation(frame1, x1[i])
        pt.add_observation(frame2, x2[i])

    for pt1, pt2 in zip(frame1.key_pts[x1], frame2.key_pts[x2]):
        u1, v1 = denormalize(K, pt1)
        u2, v2 = denormalize(K, pt2)
        cv2.circle(image, (u1, v1), color=(0,255,0), radius=1)
        cv2.line(image, (u1, v1), (u2, v2), color=(255, 255,0))

    # 2-D display
    if disp is not None:
        disp.display2D(image)
    # 3-D display
    desc_dict.display()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("%s takes in .mp4 as an arg" %sys.argv[0])
        exit(-1)
    cap = cv2.VideoCapture(sys.argv[1])
    test= Display(W,H)
    while cap.isOpened():
        ret, frame = cap.read()
        try:
            frame1 = cv2.resize(frame, (640,360)) #Resizing the original window
            if ret == True:
                cv2.imshow("Frame",frame1)    
                if cv2.waitKey(1) & 0xFF == ord('q'):   #Quit Condition
                    break
                generate_SLAM(frame)
            else:
                break
        except:
            print('Video ended')
            break
cap.release() 
cv2.destroyAllWindows()