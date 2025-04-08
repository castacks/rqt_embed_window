from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rqt_embed_window',
            executable='rqt_embed_window',
            name='rqt_embed_window_node',
            output='screen',
        ),
    ])