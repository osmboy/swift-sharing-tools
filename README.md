### Swift sharing tools

### Installation
```pip install git+https://github.com/CSCfi/swift-sharing-tools```

Contains following tools:
- swift-publish
    + share: Share an existing container to a project
    + publish: Upload and share a folder / files to a project
    + publish-request: fulfill a request for a container with specified files

### Usage
#### swift-publish
Using swift-publish requires an Openstack project file to be sourced in the
working terminal (the file containing Openstack user information for related
project). Following additional information needs to be passed via environment
variables:
```
SWIFT_SHARING_URL="http://example"; Required for sharing functionality.
SWIFT_REQUEST_URL="http://example"; Required for fulfilling sharing requests.
```

The Openstack RC file can be found from the Openstack UI, aka Horizon. It
can be found in the following location after logging in:
```
Access & Security -> API Access -> Download OpenStack RC File v3
```

After the OpenStack RC File has been downloaded, it should be run with the
following commands:
```
chmod u+x [OpenStack RC File]
. ./[OpenStack RC File]
```

Remember that the RC files are project specific, so you can't use them to
upload from anything else besides your currently active project.

Example query, for fulfilling a request for new container, with read access:
```
swift-publish publish-request container_name folder_name r
```
