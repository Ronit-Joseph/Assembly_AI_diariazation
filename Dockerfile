# Start with the specified base image  
FROM nvcr.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Set noninteractive frontend  
ARG DEBIAN_FRONTEND=noninteractive

# Update the package list and install required packages  
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    software-properties-common \
    curl \
    git

# Add the deadsnakes PPA repository and install Python 3.10  
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.10 python3.10-venv python3.10-dev

# Set the default python3 to python3.10  
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

# Install pip from official source  
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

# Add /root/.local/bin to PATH  
ENV PATH="/root/.local/bin:${PATH}"

# Cleanup  
RUN apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /

# Install the nightly version of PyTorch with CUDA 11.8 support  
RUN python3 -m pip install torch==2.0.0+cu118 torchvision==0.15.1+cu118 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu118

# Install Cython separately  
RUN python3 -m pip install --user Cython

# Install other packages from requirements.txt  
RUN python3 -m pip install --user -r requirements.txt

# Setup the workspace
WORKDIR /workspace

# Copy Protobuf files
COPY /protos .

# Expose the gRPC server port
EXPOSE 50051

# Run the gRPC server on container startup
CMD ["python3", "asr_diarization_server.py"]MQX Time To Waste