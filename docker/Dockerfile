FROM moveit/moveit2:main-jazzy-tutorial-source

RUN apt-get update && apt-get install -y \
    terminator \
    && rm -rf /var/lib/apt/lists/*

CMD [ "/usr/bin/terminator" ]