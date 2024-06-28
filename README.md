[![Ci-check](https://github.com/SugarTea2899/Azure-Devops-02/actions/workflows/pythonapp.yml/badge.svg?branch=master)](https://github.com/SugarTea2899/Azure-Devops-02/actions/workflows/pythonapp.yml)

# Overview

In this project, the objective is to develop a new GitHub repository and establish a framework that facilitates Continuous Integration and Continuous Delivery processes. This involves leveraging GitHub Actions alongside a Makefile, requirements.txt, and application code to execute an initial cycle of linting, testing, and installation. Following this, integration with Azure Pipelines will be implemented to enable seamless Continuous Delivery to Azure App Service.

## Project Plan

* [Trello Board](https://trello.com/invite/b/loFkI2UW/ATTI272f5d231ca569dc6070650bd53ab1a33788C102/azure-devops02)
* [Spreadsheet](https://docs.google.com/spreadsheets/d/1EschlFGGEW0DlrWmW1snOHnNuIjOatBz2YLb9b5T-Ws/edit?usp=sharing)

## Instructions

![Project Diagram](screenshots/diagram.png)

### Could Shell
1. SSH Key Gen:

![](screenshots/04-ssh-keygen.png)

2. Clone Repo in Could Shell:

![](screenshots/01-clone-repo.png)

3. Run `make all`:

![](screenshots/02-test-passed.png)

### GitHub Action (CI)
1. Build code successfully:

![](screenshots/03-passed-pipeline.png)

### Azure Pipeline (CD)
1. Config Agent:

![](screenshots/10-self-hosted.png)

2. Add pipeline:

![](screenshots/11-add-yaml-pipeline.png)

3. Pipeline triggered:

![](screenshots/05-azure-pipeline.png)

3. Log Stream:

![](screenshots/12-logstream.png)

4. Deploy done:

![](screenshots/06-deployed-page.png)

5. Run prediction:

![](screenshots/07-make-predict-azure-app.png)


### Load test
1. Run loadtest:

![](screenshots/08-loadtest.png)

2. Chart:

![](screenshots/09-loadtest-chart.png)

## Enhancements

- Enhancing test coverage by adding additional test cases.
- Developing a user interface for interactive prediction capabilities.
- Transitioning from Azure Pipelines to GitHub Actions - for CI/CD automation.
- Deploying the application on a Kubernetes cluster for scalable and resilient operation.

## Demo 

[My Demo](https://youtu.be/o7DAAzHWikc)


