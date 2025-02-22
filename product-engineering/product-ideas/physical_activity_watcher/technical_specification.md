# 

We are going to try and use ultra-wide-band (UWB) chips to prototype this because the UWB chips that come in phones 
have very restricted public APIs. We will need freedom to build any logic on top of the raw UWB for the sake of the POC.

Currently there are reasonably priced UWB chips available on the market such as at:
https://www.qorvo.com/products/wireless-connectivity/ultra-wideband

We just need to look into the specs and see which one we need that balances our requirements of:
- develop-ability
- location accuracy

Okay it seems that we can come to a more optimal scenario where we use inertial measurement units (IMUs) which are 
better at tracking motions from their starting point like gestures which is much more appropriate for inferring hand 
movements. While UWB is better for indoor room-scale location tracking. So a combination of these two systems 
would be better than using either alone. We can use IMUs to solve for what actions the user is performing, while using
UWB to solve for where they are doing that action in a given location.

IMU supplier:
https://www.bosch-sensortec.com/products/motion-sensors/imus/

ChatGPT Report on potential challenges and contraints:

1. Sensor Fusion Complexity:
- Combining IMU and UWB data requires an effective sensor fusion algorithm to merge the data from both systems.
This can be tricky because the two systems measure different things (position vs. orientation), and you'll need to 
ensure that they work in tandem without conflicting with each other.
- You might need to implement techniques like Kalman filtering or complementary filtering to combine the IMU data 
(which can drift) and UWB data (which can have occasional inaccuracies).

2. Drift in IMUs:
- IMUs suffer from sensor drift over time, which means their accuracy degrades unless periodically corrected. 
This can lead to a situation where the IMU will continue to track relative movement accurately, but its absolute 
position may diverge from reality if not corrected frequently.
- UWB helps correct this by providing absolute positioning, but if UWB signal strength weakens (due to obstacles or
interference), the IMU will need to help compensate.

3. Line-of-Sight and Obstacles:
- UWB performance can degrade when there are obstacles in the environment, such as walls, furniture, or even people.
UWB relies on line-of-sight between the anchor and tag for best performance. You need to ensure that the UWB system
has good coverage in the environment, or use multiple anchors to ensure reliable position tracking.
- In contrast, IMUs don’t suffer from line-of-sight issues but may need to be recalibrated periodically, especially if
there are any changes in the sensor's orientation.

4. Battery Life:
- Both IMUs and UWB sensors consume battery power. UWB systems, in particular, can be power-hungry, especially in a 
dense sensor network with many anchors and tags. IMUs are typically more power-efficient, but a system that combines
both sensors could face battery life limitations for long-term use.
- Consider low-power modes, optimized signal transmission, and possibly incorporating wireless charging solutions or
battery management strategies for long-term applications.

5. Calibration and Accuracy:
- IMUs typically need frequent calibration (especially gyroscopes) to maintain their accuracy over time. For instance,
drift correction algorithms need to be implemented.
- UWB systems may also need to be calibrated to ensure that the anchors' positions are accurately known in 3D space,
and the system must be recalibrated if the environment changes (e.g., furniture moved or obstacles added).

6. Environmental Factors:
- Environmental noise: UWB and IMUs can be susceptible to environmental interference. UWB could be affected by 
multipath (reflections of signals) or objects blocking the signal, while IMUs could be affected by things like 
vibrations or extreme temperature variations.
- Magnetic fields: For IMUs with magnetometers, nearby magnetic fields (from electronic devices, power lines, etc.)
could disturb the readings, affecting accuracy.

