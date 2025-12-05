import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'cs422_moveit2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='john',
    maintainer_email='John.McDonald@mu.ie',
    description='TODO: Package description',
    license='BSD-3-clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'full_demo = cs422_moveit2.full_demo:main',
            'pose_goal_predefined_string_1 = cs422_moveit2.pose_goal_predefined_string_1:main',
            'pose_goal_robotstate_object_2 = cs422_moveit2.pose_goal_robotstate_object_2:main',
            'pose_goal_posestamped_3 = cs422_moveit2.pose_goal_posestamped_3:main',
            'pose_goal_joint_constraints_4 = cs422_moveit2.pose_goal_joint_constraints_4:main',
            'multi_pipeline_5 = cs422_moveit2.multi_pipeline_5:main',
            'pose_goal_with_planning_scene_6 = cs422_moveit2.pose_goal_with_planning_scene_6:main',
        ],
    },
)
