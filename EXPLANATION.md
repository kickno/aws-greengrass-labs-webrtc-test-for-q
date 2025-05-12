# AWS Greengrass Labs WebRTC Application Explanation

This document provides a comprehensive explanation of the AWS Greengrass Labs WebRTC repository, its architecture, components, and how it works.

## Repository Overview

This repository contains an AWS IoT Greengrass v2 component that enables video streaming from RTSP cameras to remote viewers using Amazon Kinesis Video Streams with WebRTC. The application runs on Greengrass v2 gateway devices and acts as a bridge between IP cameras and cloud-based WebRTC viewers.

## Key Components

### 1. Architecture

The system architecture consists of:

- **Greengrass Core Device**: Runs the WebRTC component that connects to RTSP cameras
- **RTSP Cameras**: IP cameras that provide video streams via RTSP protocol
- **Amazon Kinesis Video Streams (KVS)**: AWS service that handles the WebRTC signaling and streaming
- **Remote Viewers**: Web or mobile applications that connect to the video streams via WebRTC

![Architecture Diagram](greengrass-kvswebrtc-app.png)

### 2. Component Structure

The repository is organized as follows:

- **`/source`**: Contains the C/C++ implementation of the WebRTC application
  - **`/source/src`**: Core application code that handles WebRTC, RTSP, and signaling
  - **`/source/patches`**: Patches for the Amazon Kinesis Video Streams WebRTC SDK
  - **`/source/test`**: Unit tests for the application
  - **`/source/run_webrtc.py`**: Python script that launches the WebRTC application

- **`/components`**: Contains Greengrass component definitions
  - **`/components/recipes`**: Component recipe JSON files
  - **`/components/artifacts`**: Component artifacts (binaries, scripts, etc.)

- **`/scripts`**: Helper scripts for building, deploying, and managing the component
  - **`generate-iot-greengrass.sh`**: Creates AWS resources and component artifacts
  - **`upload-component-version.sh`**: Uploads the component to AWS
  - **`deploy-component.sh`**: Deploys the component to Greengrass devices

### 3. How It Works

#### Setup and Deployment

1. The user configures RTSP camera details in a JSON configuration file (`rtsp-camera-configuration.json`)
2. The `generate-iot-greengrass.sh` script creates necessary AWS resources (S3 bucket, secrets, etc.)
3. The compiled WebRTC application is uploaded to S3 as a component artifact
4. The component is deployed to Greengrass devices using the AWS IoT Greengrass service

#### Runtime Operation

1. When the component starts on a Greengrass device, it:
   - Installs required Python dependencies (awsiotsdk, netifaces)
   - Runs the `run_webrtc.py` script with configuration parameters

2. The Python script:
   - Retrieves camera credentials from AWS Secrets Manager
   - For each configured camera, launches an instance of the WebRTC application
   - Sets environment variables for each camera (URL, credentials, channel name)

3. The WebRTC application (`awsGreengrassLabsWebRTC`):
   - Connects to the RTSP camera using GStreamer
   - Establishes a WebRTC connection through Amazon KVS
   - Forwards video frames from the RTSP stream to WebRTC viewers

### 4. Key Technologies

- **GStreamer**: Used for receiving and processing RTSP video streams
- **Amazon Kinesis Video Streams WebRTC SDK**: Handles WebRTC signaling and streaming
- **AWS IoT Greengrass v2**: Manages component deployment and lifecycle
- **AWS Secrets Manager**: Securely stores camera credentials

## Prerequisites

To use this application, you need:

1. A Greengrass v2 device with:
   - GStreamer installed (for RTSP handling)
   - Python 3 (for the component runtime)

2. AWS account with:
   - AWS CLI configured
   - Permissions to create and manage AWS resources

3. RTSP-capable IP cameras with:
   - Known URLs, usernames, and passwords

## Configuration

The application is configured through:

1. **RTSP Camera Configuration**: JSON file defining camera details:
   ```json
   {
     "RtspConfig": [
       {
         "ChannelName": "RtspCam1",
         "RtspUrl": "rtsp://camera-ip:port/path",
         "username": "camera-username",
         "password": "camera-password"
       }
     ]
   }
   ```

2. **Component Configuration**: Set during deployment:
   - `IpcTimeout`: Timeout for IPC operations
   - `RecipesBucketName`: S3 bucket for component artifacts
   - `SecretArn`: ARN of the AWS Secret containing camera credentials

## Building and Deployment

### Building the Application

1. Clone the repository and update submodules
2. Apply patches to the KVS WebRTC SDK
3. Build the application using CMake
4. Copy the binary to the artifacts directory

### Deploying the Component

1. Generate AWS resources using `generate-iot-greengrass.sh`
2. Upload the component using `upload-component-version.sh`
3. Deploy the component using `deploy-component.sh`

## Troubleshooting

Common issues and solutions:

1. **Component fails to start**: Check GStreamer installation and dependencies
2. **Cannot connect to cameras**: Verify camera credentials and network connectivity
3. **WebRTC streaming issues**: Check AWS KVS configuration and network settings

## Additional Resources

- [AWS IoT Greengrass Documentation](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)
- [Amazon Kinesis Video Streams WebRTC SDK](https://github.com/awslabs/amazon-kinesis-video-streams-webrtc-sdk-c)
- [GStreamer Documentation](https://gstreamer.freedesktop.org/documentation/)