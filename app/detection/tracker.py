import math


class Tracker:

    def __init__(self):

        self.center_points = {}
        self.id_count = 0

    def update(self, objects_rect):

        objects_bbs_ids = []

        for rect in objects_rect:
            x1, y1, x2, y2 = rect

            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            same_object_detected = False

            for obj_id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0],cy - pt[1])

                if dist < 35:

                    self.center_points[obj_id] = (cx, cy)

                    objects_bbs_ids.append([x1, y1, x2, y2, obj_id])
                    same_object_detected = True
                    break

            if same_object_detected is False:
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x1, y1, x2, y2, self.id_count])
                self.id_count += 1

        return objects_bbs_ids