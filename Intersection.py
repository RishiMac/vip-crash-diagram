import matplotlib.pyplot as plt
import Trajectory
import Lane
import numpy as np

class Intersection:
    def __init__(self, ID, name, center_point_location, num_legs, legs_collection):
        self.ID = ID
        self.name = name
        self.center_point_location = center_point_location
        self.num_legs = num_legs
        self.legs_collection = legs_collection

    def plot_trajectory():
        arr = Trajectory.compute_trajectory(Trajectory.departing_lane, Trajectory.receiving_lane)
        plt.plot(arr[0, :], arr[1, :])
    
    # plotting singular point.
    def plot_centerpoint():
        plt.plot(center_point_location[0], center_point_location[1])

    # plotting centerline for each leg.
    def plot_intersection():
        for leg in legs_collection:            
            x_values = np.empty(len(leg.leg_geometry), dtype=int)
            y_values = np.empty(len(leg.leg_geometry), dtype=int)

            xUpperEdge_values = np.empty(len(leg.leg_geometry), dtype=int)
            yUpperEdge_values = np.empty(len(leg.leg_geometry), dtype=int)
            xLowerEdge_values = np.empty(len(leg.leg_geometry), dtype=int)
            yLowerEdge_values = np.empty(len(leg.leg_geometry), dtype=int)
            #past (x1,y1) value (trying to figure out how to find edge lanes of curved paths)
            # x1 = x.leg_geometry[0]
            # y1 = y.leg_geometry[0]
            # x2 = x.leg_geometry[0]
            # y2 = y.leg_geometry[0]
            for i in range(0, len(x.leg_geometry) - 1):
                x_values[i] = leg.leg_geometry[i][0]
                y_values[i] = leg.leg_geometry[i][1]
                # trying to figure out how to find edge lanes of curved paths. 
                # if (i > 0):
                #     x1 = x2
                #     y1 = y2
                #     x2 = x.leg_geometry[i][0]
                #     y2 = x.leg_geometry[i][1]
                #     perpSlope = -(x2-x1)/(y2-y1)
            #Assuming roads are staright lines parallel to x-axis and perpendicular to y-axis.
            if y_values[0] == y_values[1]:
                for i in range(0,len(x_values) - 1):
                    xUpperEdge_values[i] = x_values[i] + leg.lane_collection[1].lane_width
                    yUpperEdge_values[i] = x_values[i] 
                    xLowerEdge_values[i] = x_values[i] - leg.lane_collection[1].lane_width
                    yLowerEdge_values[i] = x_values[i] 
            else:
                    yUpperEdge_values[i] = x_values[i] + leg.lane_collection[1].lane_width
                    xUpperEdge_values[i] = x_values[i] 
                    yLowerEdge_values[i] = x_values[i] - leg.lane_collection[1].lane_width
                    xLowerEdge_values[i] = x_values[i]                                 
           
           #lane edges
           for i in range(0, leg.lane_collection[1].lane_width):


           #plot centerline
           plt.plot(x_values, y_values) 

           #plot outer edges of lanes
           plt.plot(xLowerEdge_values,yLowerEdge_values)
           plt.plot(xUpperEdge_values,yUpperEdge_values)
