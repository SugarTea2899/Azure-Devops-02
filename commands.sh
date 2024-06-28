#!/usr/bin/env bash

az vm create --resource-group Azuredevops --name my-agent-1 --image Ubuntu2204 --size Standard_DS1_v2 --data-disk-sizes-gb 20 --admin-username devopsagent --admin-password DevOpsAgent@123 --nsg-rule SSH --public-ip-sku Standard
az webapp up --name thienflaskapp --resource-group Azuredevops --runtime PYTHON:3.9 --sku B1