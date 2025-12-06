# Create workspace folder
mkdir -p /tmp/cs422_planning/src
cd /tmp/cs422_planning/src

# Clone the cs422_moveit2 repository
git clone https://gitlab.cs.nuim.ie/johnmcd/cs422_moveit2.git

# Build the custom Docker image
cd cs422_moveit2/docker

# Build the Docker image
docker compose run --rm -v /tmp/cs422_planning:/root/cs422_planning --name moveit2_container cpu 