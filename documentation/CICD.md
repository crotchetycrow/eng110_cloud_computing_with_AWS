# CICD

## What is Continuous Integration (CI) - Continuous Delivery (CD) Continuous Deployment (CDE)

A CI/CD pipeline lets you automate steps in the software deployment process, such as initiating code builds, performing automated testing, and deploying to a staging or production environment. Automated pipelines eliminate manual errors, provide standardized development feedback loops and allow faster iterations.

### CI

Refers to Continuous Integration which is an automation process for developers. Successful CI means new code changes to an app are regularly built, tested, and merged to a shared repository.

### CD

Refers to Continuous Delivery which is related to CI and often used interchangeably. Both are about automating further stages of the pipeline but CD usually means a developer's changes to an application are automatically bug tested and uploaded to the repository, where they can be deployed to a live production environment by the operations team.

The purpose of CD is to ensure that it takes minimal effort to deploy new code.

### CDE

Refers to Continuous Deployment where a developers changes are automatically released from the repository to production where it is used by customers.

It addresses the problem of overloading the operations teams with manual processes that slow down app delivery. It builds on the benefits of continuous delivery by automating the next stage in the pipeline.

## What is the difference between CD and CDE

The delivery process is the process during which you are coordinating the delivery of the item by entering your address and confirming when you want your item delivered.

Once the package arrives you will inspect it. If you’re happy with it, you can start using it. That’s deployment. If you are not happy with the item, you can reject it and send it back. This can be compared to your code failing an automated test, which means that it would be sent back to your developers instead of being deployed to your clients so that they can start taking advantage of the changes right away.

This means that continuous deployment represents the full, complete, end-to-end development pipeline. And the main difference between continuous deployment and delivery is that releases happen automatically in continuous deployment if all criteria for the release are met through testing.

## What is Jenkins and the benefits of using it

Jenkins is a self-contained, open-source automation platform written in Java with plugins designed for CI/CD pipeline. Jenkins is used for building and testing the software application continuously.

It eases the developer’s work of integrating the code changes to the project so the users can obtain a fresh build. Jenkins also helps in Continuous Delivery of applications by integrating with a wide variety of testing and deployment technologies.

### Benefits:

- Jenkins is an open-source tool that is extremely easy to install and use. You need no extra components to use it
- It is free and available to be used with different platforms, such as Windows, Linux, macOS, and others
- Jenkins automates all integration work. Integration issues are scarce, and so, it helps in saving time and money over the project lifecycle.
- It is easy to configure, extend, and modify. It allows the instant generation of tests and building, automation, and deployment of code on different platforms
- Jenkins can be configured to run CI and CD concepts properly
- It can easily detect and fix issues. The software is always ready for a sudden release
- Supports a variety of plugins, which allows better flexibility
- It helps in detecting errors very early, thus saving developers a lot of time and hard work

## What is SDLC using Jenkins

- First, the developer commits the code changes to the source repository.
- Jenkins server checks the repository frequently for the new changes.
- The Jenkins server detects the changes that have occurred in the source code repository soon after a commit occurs. Then, Jenkins pulls out those changes and start preparing a new build.
- If the build fails, it intimates the concerned teams regarding the build failure.
- If the build is a success, Jenkins deploys the code in the test server.
- After testing, Jenkins sends feedback to the developers regarding build and test results.
- Jenkins looks for the source code repository for changes and the whole process repeats.

## What other tools are there in the industry for CICD

- Spinnaker, a CD platform built for multicloud environments.
- GoCD, a CI/CD server with an emphasis on modeling and visualization.
- Concourse, "an open-source continuous thing-doer."
- Screwdriver, a build platform designed for CD.

![](../img/ci-cd-flow.png)
