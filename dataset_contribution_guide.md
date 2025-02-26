# Dataset Contribution Guide

To contribute your own data, we have provided several tools to help in ensuring your dat has the correct formatting.

## File naming convention

When naming video files, they must follow the filename nomenclature:
* **{action}\_{environment}\_{diver-orientation}\_{unique-10-digit-hash}.{video-filetype}**
    * **action:** refers to the specifc action/gesture that is demonstrated in the video. For example, OKAY, BUDDYUP, or RIGHT
    * **environment:** refers to the general location class of where the diver is. Options are:
        * TANK: if in testing water tank. Use if in tank with bland/ sterile background
        * AQUARIUM: if in an aquarium (meaning backgorund consists of fish, structures, etc.)
        * SEA: use if in open water environment
        * SPRINGS: Use if diving in a spring
        * REEF: if reef diving, coral reef or other underwater ocean structure
        * *Modifiers*: (for environment, a modifier can be added to environment. For example, AQUARIUM-LOWVIZ)
            * **LOWVIZ**: use if the visibility is exceptionally low
            * **LOWLIGHT**: use if the light is exceptionally low
    * **Diver-orientation:** refers to whether the data is collected when the diver is in a horizontal or vertical position
    * **video-filetype:** can be ".MP4" or ".mp4"

## General Data Collection Tips

* Ensure diver is in center of frame, and camera is facing the diver. Recording at 1-2 arms-lengths from the diver is recommended for best results.
    * *By recording in this setting, we follow the idea that action recognition should occur after the robot has used other means to position itself in front of the diver, where it can most easily see the gesture the diver is trying to make.*
