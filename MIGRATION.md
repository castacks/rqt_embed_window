# ROS1 to ROS2 Migration Notes

This document outlines the changes made to migrate the `rqt_embed_window` package from ROS1 to ROS2 Humble.

## Changes Made

### Package Configuration
- Updated `package.xml` from format 2 to format 3
- Changed build tool dependencies from `catkin` to `ament_cmake` and `ament_cmake_python`
- Updated dependencies from `rospy` to `rclpy`
- Added explicit dependency on `python3-qt5`
- Fixed package name tag (was `<n>` instead of `<name>`)

### Build System
- Updated `CMakeLists.txt` to use ROS2 conventions
- Changed from `catkin_python_setup()` to `ament_python_install_package()`
- Updated installation paths to follow ROS2 conventions
- Added testing support

### Python Code
- Updated shebang lines from `python` to `python3`
- Updated imports from `rospy` to `rclpy`
- Updated logging from `rospy.logerr` to `rclpy.logging.get_logger().error`
- Added proper decoding of subprocess output for Python 3 compatibility
- Updated print statements to use parentheses for Python 3 compatibility

### Launch Files
- Created new Python-based launch files for ROS2
- Kept original XML launch files for reference

### Documentation
- Updated README with ROS2 usage instructions
- Added migration notes

## Testing
- Added basic import tests to verify package structure

## Future Improvements
- Consider using ROS2 parameters instead of QInputDialog for configuration
- Implement lifecycle nodes for better resource management
- Add more comprehensive testing