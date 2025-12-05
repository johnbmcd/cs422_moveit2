FROM moveit/moveit2:main-jazzy-tutorial-source

RUN apt-get update && apt-get install -y \
    terminator \
    dbus-x11 \
    libcanberra-gtk3-module\
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /etc/xdg/terminator/
RUN touch /etc/xdg/terminator/config

COPY ros_entrypoint.sh /ros_entrypoint.sh

WORKDIR /root/cs422_planning

CMD [ "/usr/bin/terminator" ]