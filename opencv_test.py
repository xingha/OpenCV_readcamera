# -*- coding:utf-8 -*-
# Author : Mr Zhou
# Date : 2019/05/15

import cv2


RTSP_SOURCE = 'rtsp:'


def grab_pic(camera, times):
    success, frame = camera.read()
    if not success and times > 0:
        grab_pic(camera, times - 1)
    elif success:
        return success, frame
    else:
        return None, None


def read_camera(source):
    cam = cv2.VideoCapture()
    while True:
        cam.open(source)
        print("print camera ...")
        while True:
            success, frame = grab_pic(cam, 3)
            if success:
                cv2.imshow("frame", frame)
                cv2.waitKey(1)
            else:
                break
    cam.release()
    return 0

if __name__ == "__main__":
    read_camera(RTSP_SOURCE)