# Problem Document - Capture Data From Physical Activities

## Central problem
I want to be able to measure where I spend my time and what I do in the physical world so I can assess my own
workflows and thus introduce efficiencies. This is currently a manual task which requires myself to be conscientious
of what I do and when I do it and for how long. I don't have the energy nor time to always track this manually.
I want there to be an independent system which can autonomously do this for me so that I can look at the data later
to make assessments and even layer a assessment program or logic over the empiric and accurate data.

## Problem characteristics
Number of users this problem applies to (high | mid | low): mid
Frequency a user will experience this problem (high | mid | low): mid

## Current Best Solutions
Wearables like:
apple watch
hand motion game controllers (wii, ps vr, etc.)
motion capture technology

Nothing really allows me to capture my 3-dimensional hand movements and location to tell me what I'm doing, in 
which location.

# Observations
The current ideal form-factor which I think introduces minimal change to a user's attire and would provide enough data
would be dual-wrist bands. They ideally would be able to capture 3-dimensional hand movements. This would allow 
enough data (I think) to let us infer what activity is being performed. Especially when paired with data points from 
other participant devices like the user's phone and PC.

There is enough rough idea as to what we need to investigate to establish some kind of cheap way to resolve 
hand positions. If we have the user's phone as a participant, plus the two wrist bands. Those 3 devices may be able
to triangulate each other's positions (not sure to how accurate of a degree and what the caveats will be).

We also need to consider how we will find the user's coordinates indoors. Outdoors is easy thanks to GPS. However
indoors GPS is not viable. There is the concept of wifi-trilateration/bluetooth which thoerizes the use of indoor signals to 
perform the same function that GPS does outdoors. We need to look into this and know exactly how many hardware devices
besides just the router will be needed for the user to setup to achieve this.

With this in mind. If we can resolve the 3-dimensional position of the user indoors with some kind of wifi-trilateration
plus the triangulation between their phone and wrist-bands to determine what they are doing with their hands.
We may be able to resolve where they are in physical space, and how they are using their hands to perform various 
activities.

Basically will act as a broad master watcher that is dumb and just collects as much data as possible on the users 
activities as cheaply as possible.

# Ideal solution

## Feature Backlog

