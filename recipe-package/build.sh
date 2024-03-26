#!/bin/bash

REPO_URL=${REPO_URL}
BRANCH_NAME=${BRANCH_NAME:-main}
WORKDIR_PATH=${WORKDIR_PATH}
RECIPE_NAME=${RECIPE_NAME}
GIT_COMMIT_SHA=`git ls-remote ${REPO_URL} ${BRANCH_NAME} | awk '{ print $1 }'`
# Check if it already exists

# Build the Docker image
docker build --build-arg REPO_URL=$REPO_URL \
             --build-arg BRANCH_NAME=$BRANCH_NAME \
             --build-arg WORKDIR_PATH=$WORKDIR_PATH \
             -t ${RECIPE_NAME}-${GIT_COMMIT_SHA} .