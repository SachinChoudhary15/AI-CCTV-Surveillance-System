
import cv2
import time


class FPSCounter:

    def __init__(self):

        self.prev_time = 0
        self.curr_time = 0

    def update_fps(self):

        self.curr_time = time.time()
        fps = 1 / (self.curr_time - self.prev_time)
        self.prev_time = self.curr_time

        return int(fps)

    def draw_fps(self, frame, fps):

        cv2.putText(frame, f"FPS: {fps}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        return frame