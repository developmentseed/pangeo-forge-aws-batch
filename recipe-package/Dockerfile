# Use the Apache Beam Python SDK as the base image
FROM apache/beam_python3.10_sdk:2.52.0

# Install Git
RUN apt-get update && \
    apt-get install -y git

# Environment variables for the repository and branch to clone
ARG REPO_URL
ARG BRANCH_NAME=main
ARG WORKDIR_PATH=.

# Clone the specified repository and branch
RUN git clone -b ${BRANCH_NAME} ${REPO_URL} /repo

# Change the working directory
WORKDIR /repo/${WORKDIR_PATH}

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the runner script into the image
COPY run.py /repo

# Set the command to run the runner script
CMD ["python", "/repo/run.py"]

# docker run -e AWS_ACCESS_KEY_ID=XXX \
#   -e AWS_SECRET_ACCESS_KEY=XXX \
#   -e AWS_SESSION_TOKEN="XXX" \
#   --entrypoint /bin/sh \
#   -it mursst-kerchunk-XXX
