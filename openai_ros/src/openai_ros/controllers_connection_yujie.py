#!/usr/bin/env python 

# turtlebot and Husky do not need the controller_manager
import time
import rospy
import time
from controller_manager_msgs.srv import SwitchController, SwitchControllerRequest, SwitchControllerResponse

class ControllerConnection():
    def __init__(self, namespace, controllers_list):

        rospy.logwarn("Start Init Controllerconnection")
        self.controlllers_list = controllers_list
        self.switch_service_name = '/'+ namespace+'/controller_manager/switch_controller'
        self.switch_service = rospy.ServiceProxy(self.switch_service_name, SwitchController)