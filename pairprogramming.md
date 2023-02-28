---
title: Pair Programming
description: "Pair programming is a technical practice in which two engineers jointly produce one artifact together. Pair programming serves many purposes such as knowledge sharing between engineers, peer review of work produced, and to reinforce good programming principles between engineers."
excerpt: "Pair programming is a technical practice and an excellent method to achieve: Knowledge sharing, Synchronous code review, New team member onboarding, Feature demonstration. Pair programming is an optional practice, not to be looked at as mandatory."
publish_date: '2021-09-01'
last_updated: "2022-03-14"
---

## Overview
Pair programming is a technical practice in which two engineers work together to  collaberatively produce one artifact. Usually, two engineers use one computer, sharing the keyboard. Both engineers must share their thoughts while working together.

### Why Pair Programming
Pair programming is a beneficial technical practice that the product team can
engage in to increase team product knowledge, problem solving and awareness of
critical issues, and to maintain team health.
- Synchronous code review - while working together immediate feedback is shared,  which helps team to fix problems quickly.
- Collective ownership of code - Since two engineers working together have collective responsibility, also increase code quality and test coverage.
- Knowledge sharing - While pairing knowledge has been shared between engineers.
- Low WIP - since code quality increases which reduces the Work in progress tasks.
- Onboarding new members - better way to onboard new member is to start pairing with engineers, knowledge has been shared quickly and new member will be productive as well.
- Isolate and solve a complicated or critical problem - fixing the issues with two minds work together.
- Demonstrate new features and functionality.

## How to Pair

### Pairing Strategies

  - Driver and Navigator
      - The **Driver** is the one who write the code and focused on completing the task, ignoring larger issues at the moment.
      - The **Navigator** is the Observer, while Driver working on the task, Navigator reviews the code on-the-go, gives directions and share thoughts. The Navigator also has an eye on the larger issues, bugs and discuss next potential steps.
  - Ping Pong
      - **Ping**: Developer 1 starts writing failing test case
      - **Pong**: Develeoper 2 writes the implementation of code to make test pass and  refactor the code to make it perfect.
  - Strong style
      >"For an idea to go from your head to the computer it MUST go through someone else's hands." - Llewellyn Falco

In strong style pairing driver does nothing that the navigator did not tell them to do. In this model the driver is novice and the navigator is more experienced. In some cases, experience person stays longer in navigator role and guides the novice.  This style is very useful for initial knowledge transfer and upskilling new members.


Consider below when pairing up:

1. Pair up the more senior engineers with the more junior engineers to
   transfer product knowledge between senior and junior
   engineers.
2. Pair up two senior level engineers to solve specific task, other engineers can watch how the pair is effectively collaborating, code review by giving immediate feedback while solving the task.

## When to Pair
- Knowledge sharing - having a senior developer work with a more junior developer on a piece of code helps to spread product knowledge.
- Synchronous code review - In critical situations pair programming is a great way to get a quick code review.
- Low WIP - Limiting the work in progress is a core principle of Kanban in order to improve team flow.
- Onboarding new members - Pair programming is an excellent way to get a new developer up to speed on the product code base.
- Isolate and solve a complicated or critical problem.
- Demonstrate new features and functionality.

## Dos and Don'ts

### Do's
- Set Ground rules for pairing: work out on the logistics, how and when to pair. Agree on timings.
- Switch pairs often. Teams has different opinion on when to switch pairs, ideal recommendation is 2-3 days.
- Expect a learning curve at the beginning. It takes a bit of time to figure out how to work with every other developer in the team.
- Pairing is draining so make sure to take adequate breaks. Employ time management techniques like pomodoro do mange breaks.


### Don'ts
- Overdo it. Pairing 6 hours is plenty. We may need to do other stuffs like checking email, 1:1s, meetings, and learnings.
- Let the pairing stagnate. Don't let two developers always pair this will create knowledge silos within the team. Make sure everyone is getting a chance to work with all other members on the team.
- Leap on errors quickly and give low level instructions to the driver.
- Let one person dominate the entire session. Pairs should be comfortable grabbing keyboard and contribute their ideas.

## Additional Resources

- [On Pair Programming](https://martinfowler.com/articles/on-pair-programming.html), by Birgitta Bocker and Nina Siessegger, 15 Jan 2020
- [Pair Programming Wikipedia](https://en.wikipedia.org/wiki/Pair_programming), Wikimedia Foundation, 18 Dec. 2020.
- [Extreme Programming Explained: Second Edition, Embrace Change](https://www.amazon.com/Extreme-Programming-Explained-Embrace-Change/dp/0321278658), by Kent Beck and Cynthia Andres, Addison-Wesley, 2015, pp. 42-44.
- [Clean Agile: Back to Basics](https://www.amazon.com/Clean-Agile-Basics-Robert-Martin/dp/0135781868), by Robert C. Martin, Pearson, 2020, pp. 127-131.
- [Pair Program kata-log](https://kata-log.rocks/pair-programming)
