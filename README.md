## Install Dependencies

Execute the following commands:<br>
`cd ~/ros_ws/src`<br>
`git clone https://bitbucket.org/theconstructcore/openai_ros.git`<br>
`cd ~/ros_ws`<br>
`catkin_make`<br>
`source devel/setup.bash`<br>
`rosdep install openai_ros`<br>


## Use
See another repository<br>

## 
Change the original "theconstructcore" version. It works with ROS Noetic, Ubuntu 20,04 now.<br>
You can test it with <br>
`roslaunch cartpole_openai_ros_examples start_training_n1try_2D.launch`<br>
`roslaunch my_turtlebot2_training start_training.launch`<br>




