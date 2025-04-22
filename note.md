# MetaUrban

## Environment
- static or dynamic environment
- how to create or change environment setting?
- Bullet point 3

## agent definition
- types of agent
- agent control / action space
- agent observation
    - lidar (271,)
        - ego state - dim>=9
            - steering, heading, velocity and relative distance to boundaries
        - navigation - dim=10
        - lidar - dim=240 for single agent; dim=70 for multi-agent
    - all (lidar + rgb + depth + semantic)
        - image (1080, 1920, 3, 3)
        - state (271,)
        - depth (640, 640, 1, 3)
        - semantic (640, 640, 3, 3)

## navigation
- as part of the lidar input, which contains 2 or more future checkpoints
- checkpoints are calculated based on routing 

## components
- pedestrian
- delivery robot
- vehicles
- robot dog

## reward function
- driving
- lane keeping
- steering smoothness
- crash penalty
- termination reward


## challenge
- graph, communication topology
- which one is useful
