#!/usr/bin/env python

import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Callbacks definition

def active_cb():
    rospy.loginfo("Goal pose being processed")

def feedback_cb(feedback):
    # rospy.loginfo("Current location: "+str(feedback))
    pass


def done_cb(status, result):
    if status == 3:
        rospy.loginfo("Goal reached")
    if status == 2 or status == 8:
        rospy.loginfo("Goal cancelled")
    if status == 4:
        rospy.loginfo("Goal aborted")
    

rospy.init_node('goal_pose')



def moveToPose(x, y, z, qx, qy, qz ,qw):
    # 7th intermediate pose
    navclient = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    navclient.wait_for_server()


    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.position.z = z
    goal.target_pose.pose.orientation.x = qx
    goal.target_pose.pose.orientation.y = qy
    goal.target_pose.pose.orientation.z = qz
    goal.target_pose.pose.orientation.w = qw

    navclient.send_goal(goal, done_cb, active_cb, feedback_cb)
    finished = navclient.wait_for_result()

    navclient.wait_for_server()
    if not finished:
        rospy.logerr("Action server not available!")
    else:
        rospy.loginfo ( navclient.get_result())


rospy.loginfo("moving to point 1 \n")
moveToPose(-0.41653275707331805, -1.4154201018296793, 0, 0, 0, 0.22396615365457775, 0.9745969228440925)
rospy.loginfo("moving to point 2 \n")
moveToPose(-0.4334241370318591, -0.8816998944260365, 0, 0, 0, 0.995305045612146, 0.09678773775124486)
rospy.loginfo("moving to point 3 \n")
moveToPose(-1.6221994296450517, 0.04234088489675708, 0, 0, 0, 0.9999367161939051, 0.011250049215433884)
rospy.loginfo("moving to point 4 \n")
moveToPose(-2.4601872433805387, 0.024421546102352868, 0, 0, 0, -0.6808380447902653, 0.7324339948187609)
rospy.loginfo("moving to point 5 \n")
moveToPose(-3.143371497110827, -0.8116416228435321, 0, 0, 0, 0.02309394928508573, 0.9997332991885475)
rospy.loginfo("moving to point 6 \n")
moveToPose(-1.8542433905782134, -1.0424378012253894, 0, 0, 0, -0.7438023375994037, 0.6683996428647031)
rospy.loginfo("moving to point 7 \n")
moveToPose(-3.0322979114198474, -1.4307653575331425, 0, 0, 0, -0.7573886161546503, 0.6529643819683765)
rospy.loginfo("moving to point 8 \n")
moveToPose(-3.107166976223418, -1.8118033874259067, 0, 0, 0, -0.003135077343597583, 0.9954756891972948)
rospy.loginfo("moving to point 9 \n")
moveToPose(-2.3315543532942247, -2.292371256232144, 0, 0, 0, 0.02906033382073213, 0.999577659313286)
rospy.loginfo("moving to point 10 \n")
moveToPose(0.32680405676279867, -2.2651931440929363, 0, 0, 0, 0.6536735969770596, 0.8188172874909201)
rospy.loginfo("moving to point 11 \n")
moveToPose(0.43795675726065514, 0.07410791927886035, 0, 0, 0, 0.9825849890050594, 0.18581372226487267)
rospy.loginfo("moving to point 12 \n")
moveToPose(-0.1475594202556791, 0.08120611811364793, 0, 0, 0, -0.7253779824318728, 0.6883507700315775)
rospy.loginfo("moving to point 13 \n")
moveToPose(-0.9954095476799393, -1.4017364879689138, 0, 0, 0, 0.08184743992911987, 0.996644869839327)
