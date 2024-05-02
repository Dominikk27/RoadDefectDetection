import math

class Tracker():
    def __init__(self):
        self.center_points = {}
        self.id_count = 0
        

    
    def update(self, objectBox):
        if not objectBox:
            return []

        objects_boxes_id = []
        same_detection = False

        for box in objectBox:
            x, y, w, h = box
            cx = (x+x+w) 
            cy = (y+y+h)


            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 50:
                    self.center_points[id] = (cx, cy)
                    objects_boxes_id.append([x, y, w, h, id])
                    same_detection = True
                    break
                
        if not same_detection:
            self.center_points[self.id_count] = (cx, cy)
            objects_boxes_id.append([x, y, w, h, self.id_count])
            self.id_count += 1

        new_center_points = {}
        for obj_box_id in objects_boxes_id:
            _, _, _, _, object_id = obj_box_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center
        
        self.center_points = new_center_points.copy()
        return objects_boxes_id