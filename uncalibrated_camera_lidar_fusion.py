# Uncalibrated Camera-LiDAR Fusion Demo
# Assumptions:
# - Logitech C920 1280x720 (~78 deg HFOV)
# - RPLIDAR A1M8
# - YOLOv8 TensorRT engine: yolov8n.engine
# NOTE: Projection is approximate and intentionally uncalibrated.

import cv2, time, math, threading
from ultralytics import YOLO
from rplidar import RPLidar

ENGINE="yolov8n.engine"
LIDAR_PORT="/dev/ttyUSB0"
WIDTH,HEIGHT=1280,720
HFOV=78.0

model=YOLO(ENGINE)
lidar=RPLidar(LIDAR_PORT)
scan=[]
lock=threading.Lock()

def lidar_thread():
    global scan
    for s in lidar.iter_scans():
        pts=[]
        for _,ang,dist in s:
            if dist<=0: continue
            a=math.radians(ang)
            x=dist*math.sin(a)
            z=dist*math.cos(a)
            pts.append((x,z,dist))
        with lock:
            scan=pts

threading.Thread(target=lidar_thread,daemon=True).start()

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,HEIGHT)
fx=(WIDTH/2)/math.tan(math.radians(HFOV/2))
cx,cy=WIDTH//2,HEIGHT//2
prev=time.time()

while True:
    ok,frame=cap.read()
    if not ok: break
    with lock:
        pts=list(scan)
    imgpts=[]
    for x,z,d in pts:
        if z<100: continue
        u=int(fx*(x/z)+cx)
        v=cy
        if 0<=u<WIDTH:
            imgpts.append((u,v,d))
            cv2.circle(frame,(u,v),2,(0,0,255),-1)
    res=model(frame,verbose=False,classes=[0,2,5,7])
    ann=res[0].plot()
    for b in res[0].boxes:
        x1,y1,x2,y2=map(int,b.xyxy[0])
        ds=[p[2] for p in imgpts if x1<=p[0]<=x2 and y1<=p[1]<=y2]
        if ds:
            cv2.putText(ann,f"{min(ds)/1000:.2f} m",(x1,max(20,y1-5)),
                        cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,255),2)
    now=time.time();fps=1/(now-prev);prev=now
    cv2.putText(ann,f"FPS {fps:.1f}",(10,25),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,0),2)
    cv2.imshow("Uncalibrated Fusion",ann)
    if cv2.waitKey(1)&0xFF==ord('q'): break

cap.release()
lidar.stop(); lidar.disconnect()
cv2.destroyAllWindows()
