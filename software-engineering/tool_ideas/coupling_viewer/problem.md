# Problem Document - Coupling Viewer

## Central problem
All architecture especially for making sure that code is not too tightly coupled, is usually all done in the head of a 
senior engineer or architect. This is a tool to help visualize the coupling between classes and packages in a codebase. 
It will be a tool that gives structure by identifying "green" scopes of the code that are cohesive allowing for localized changes to be made.
While it also identifies "red" scopes of the code that are coupled. 

This gives the developer a clear view of what changes your codebase will allow you to make easily vs what will be hard to change.
This gives an architect a sense of cost of change and allows them to prioritize tech debt decoupling decisions based on 
business requirements.

## Current Best Solutions
🔹 Structure101
Purpose: Visualizes dependency graphs and identifies excessive coupling.
Best For: Large projects that need refactoring.
Website: structure101.com
🔹 SonarQube
Purpose: Detects high coupling, cyclic dependencies, and code smells.
Best For: Teams that need ongoing monitoring of tech debt.
Website: sonarqube.org
🔹 NDepend (for .NET) & JDepend (for Java)
Purpose: Measures coupling and cohesion metrics.
Best For: Developers using .NET (NDepend) or Java (JDepend).
Website: ndepend.com, jdepend.org
🔹 CodeScene
Purpose: Uses behavioral code analysis to find hotspots of high coupling.
Best For: Teams that want to factor in developer activity (not just static analysis).
Website: codescene.com

# Observations

# Ideal solution

## Feature Backlog

