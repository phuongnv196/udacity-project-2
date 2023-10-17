

## Overview

In this project, We will build a Github repository from scratch and create a scaffolding in performing both Continuous Integration and Continuous Delivery.
- Using Github Actions along with a Makefile, requirements.txt and application code to perform an initial lint, test, and install cycle.
- Integrating this project with Azure Pipelines to enable Continuous Delivery to Azure App Service.
- Using Azure Cloud shell in this project.

## Project Plan

- [Trello Board](https://trello.com/b/umdJDZJw/udacity-project-2)
- [Original Project Plan](documents/OriginalProjectPlan.xlsx)
- [Final Project Plan](documents/FinalProjectPlan.xlsx)

## Architecture Diagram

[Architectural Diagram](screenshots/architecture.png)

## Instructions
### Configuring Github

- Log in Azure Portal and access Azure Cloud Shell

- Create a ssh key by using this command:

    ```bash
    ssh-keygen -t rsa -b 2048 -C "phuongnv1996@outlook.com"
    ```

    ![SSH Key Create](screenshots/az-ssh.png)

- Copy the public key to Github Account -> Settings -> SSH and GPG keys (https://github.com/settings/keys)

    ![Setting SSH Key in Github](screenshots/github-setting-ssh.png)


### Project Locally

- After setting SSH key in Github, we can clone source code to Azure Cloud Shell by using command below: 

    ```bash
    git clone git@github.com:phuongnv196/udacity-project-2.git
    ```

    ![Clone git source code](screenshots/github-clone-success.png)

- Create a Python Virtual Environment to run your application

    ```bash
    python3 -m venv ~/.udacity-project-2
    source ~/.udacity-project-2/bin/activate
  ```
    ![Install dependencies](screenshots/az-create-inv.png)
                                  

- Install all dependencies by using **make**
    ```bash
    make all
    ```

    ![Install dependencies](screenshots/az-install-dependencies.png)

- Run application using **flask**
    ```bash
    export FLASK_APP=app.py
    flask run
    ```
    
  ![Local run](screenshots/az-flask-run.png)                                                                   

- After run application we had to open new tab and lauch a new Azure Cloud Shell session to test the application by running the *make_prediction.sh* script
    ```bash
    chmod +x make_prediction.sh
    ```
    ```bash
    ./make_prediction.sh
    ```                               

    We can see the result of script: 
    ```bash
    ./make_prediction.sh
    ```      

    ![Make prediction result](screenshots/az-make-prediction-result.png)  


Azure App Service is a cloud platform service (PaaS) offered by Azure that allows you to easily and quickly deploy web applications, mobile back-ends and RESTful APIs without worrying about the infrastructure. Some of the benefits of using Azure App Service are:

- It supports multiple programming languages (Java, Python, C#) and frameworks (.NET, Spring boot, Flask), giving you the flexibility to choose the best tools for your project.
- It provides high availability and scalability, ensuring that your applications can handle high traffic and demand without downtime or performance issues.
- It supports both Windows and Linux operating systems, enabling you to run your applications on the platform of your choice.
- It integrates very well with Azure pipelines for continuous delivery, allowing you to automate the deployment process and deliver updates faster and more reliably.
For more information and tutorials on how to use Azure App Service, please visit this [link](https://docs.microsoft.com/en-us/azure/app-service/).


#### ML Azure App Service
Azure App Service provides various options to create a new application. In this section, you will learn how to use the Azure CLI to deploy your app. In another section, you will see how to use Azure Pipelines to automate the deployment process.                                          
**Set up Azure CLI:**

- Create a new Resource Group for our app

   ```bash
    az group create --location westeurope --resource-group phuongnv_rg_02 --tags project=udacity_p_2 environment=dev
    ```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              