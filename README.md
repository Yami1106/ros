<div align="center">

# ROS Autonomous Navigation Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![ROS](https://img.shields.io/badge/ROS-22314E?style=for-the-badge&logo=ros&logoColor=white)](https://ros.org)

*Differential drive and skid-steer robots with full autonomous navigation: SLAM, Gmapping, obstacle avoidance, and mapping — simulated in Gazebo.*

</div>

---

## Overview

Built as part of the RigBetel Labs ROS Mentorship Program. Implements complete autonomous navigation stacks for two robot types from scratch, covering the full pipeline from sensor data to navigation decisions.

---

## Robots

### Differential Drive Robot
- Standard two-wheel drive with odometry
- Sensor fusion from lidar + wheel encoders
- Obstacle avoidance with reactive behaviours

### Skid-Steer Robot
- Four-wheel skid steering for indoor navigation
- Higher stability and payload capacity
- Tuned for confined-space mapping

---

## Navigation stack

```
Lidar + Odometry → Gmapping SLAM → Occupancy Grid Map
                                 → AMCL Localisation
                                 → Navigation planner (move_base)
                                 → Obstacle avoidance → Motor commands
```

---

## Features

- **SLAM** with Gmapping — builds map while navigating
- **Autonomous obstacle avoidance** using lidar data
- **ROS pub-sub architecture** — modular, extensible node design
- **Custom launch files** and parameter configurations
- **Gazebo simulation** with realistic physics

---

## Tech stack

`Python` · `ROS (Noetic)` · `Gazebo` · `Gmapping` · `AMCL` · `move_base`

---

<div align="center">
RigBetel Labs ROS Mentorship Program · <a href="https://github.com/Yami1106">Ashish Sukumar</a>
</div>
