FROM nexus.engageska-portugal.pt/ska-docker/tango-cpp:latest

ADD data/hdbpp_es_Makefile .
ADD data/PushThread.h .
ADD data/hdbpp_cm_Makefile .
ADD data/HdbConfigurationManager.h .
ADD data/libhdbpp-mysql_Makefile .
ADD data/LibHdb++MySQL.h .
ADD data/LibHdb++Cassandra.h .
ADD data/devices.json .

# Install git
ENV DEBIAN_FRONTEND noninteractive
USER root
RUN apt-get update
RUN apt-get install -y --force-yes git
RUN apt-get install -y --force-yes cmake
RUN apt-get install -y --force-yes g++
#RUN apt-get install -y --force-yes gcc
RUN apt-get install -y --force-yes wget
RUN apt-get install -y --force-yes default-libmysqlclient-dev

RUN gcc -v


#ARG tango_install_dir=/usr/local/tango-9.2.5a
#ARG tango_lib_path=/usr/local/tango-9.2.5a/lib
#ARG tango_include_path=/usr/local/tango-9.2.5a/include/tango
#ARG omniORB_install_dir=/usr/local/omniORB-4.2.1
#ARG omniORB_include_path=/usr/local/omniORB-4.2.1/include
#ARG omniORB_library_path=/usr/local/omniORB-4.2.1/lib
#ARG ZMQ_install_dir=/usr/local/tango-9.2.5a
#ARG ZMQ_include_path=/usr/local/zeromq-4.0.5/include
#ARG ZMQ_library_path=/usr/local/tango-9.2.5a/lib

ENV PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
#ENV PKG_CONFIG_PATH=/usr/local/tango-9.2.5a/lib/pkgconfig

#RUN find / -iname tango.h
#RUN ls -l /usr/local/lib

# Install libuv 1.4.2
# libuv_1.4.2-1_amd64.deb
RUN wget --no-check-certificate https://downloads.datastax.com/cpp-driver/ubuntu/14.04/dependencies/libuv/v1.4.2/libuv_1.4.2-1_amd64.deb && \
    find / -iname libuv_1.4.2-1_amd64.deb && \
    dpkg -i --force-overwrite /libuv_1.4.2-1_amd64.deb && \
    apt-get install -f
# libuv-dev_1.4.2-1_amd64.deb
RUN wget --no-check-certificate https://downloads.datastax.com/cpp-driver/ubuntu/14.04/dependencies/libuv/v1.4.2/libuv-dev_1.4.2-1_amd64.deb && \
    find / -iname libuv-dev_1.4.2-1_amd64.deb && \
    dpkg -i --force-overwrite /libuv-dev_1.4.2-1_amd64.deb && \
    apt-get install -f

# Install libssl1.0.0
# cassandra-cpp-driver depends on libssl1.0.0 (>= 1.0.0)
RUN wget --no-check-certificate http://security.debian.org/debian-security/pool/updates/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u11_amd64.deb && \
    find / -iname libssl1.0.0_1.0.1t-1+deb8u11_amd64.deb && \
    dpkg -i --force-overwrite /libssl1.0.0_1.0.1t-1+deb8u11_amd64.deb && \
    apt-get install -f

# Install Cassandra C++ driver 2.2.1
# cassandra-cpp-driver_2.2.1-1_amd64.deb
RUN wget --no-check-certificate https://downloads.datastax.com/cpp-driver/ubuntu/14.04/cassandra/v2.2.1/cassandra-cpp-driver_2.2.1-1_amd64.deb && \
    find / -iname cassandra-cpp-driver_2.2.1-1_amd64.deb && \
    dpkg -i --force-overwrite /cassandra-cpp-driver_2.2.1-1_amd64.deb && \
    apt-get install -f
# cassandra-cpp-driver-dev_2.2.1-1_amd64.deb
RUN wget --no-check-certificate https://downloads.datastax.com/cpp-driver/ubuntu/14.04/cassandra/v2.2.1/cassandra-cpp-driver-dev_2.2.1-1_amd64.deb && \
    find / -iname cassandra-cpp-driver-dev_2.2.1-1_amd64.deb && \
    dpkg -i --force-overwrite /cassandra-cpp-driver-dev_2.2.1-1_amd64.deb && \
    apt-get install -f

# Install libhdbpp
RUN mkdir hdb++ && \
    cd hdb++ && \
    git clone https://github.com/tango-controls-hdbpp/libhdbpp.git && \
    cd libhdbpp && \
    mkdir build && \
    cd build && \
    cmake -DCMAKE_INCLUDE_PATH="/usr/local/include/tango;/usr/local/include" -DCMAKE_LIBRARY_PATH=/usr/local/lib .. && \
    make && \
    make install

# Copy LibHdbpp Lib files in /usr/local/lib
RUN cp /hdb++/libhdbpp/lib/* /usr/local/lib

RUN find / -iname libhdbpp
RUN ls /hdb++/libhdbpp
RUN ls /usr/local/lib
RUN find / -iname tango.h

    
# Install hdbpp-es
RUN cd /hdb++ && \
    git clone https://github.com/tango-controls-hdbpp/hdbpp-es.git && \
    cd hdbpp-es && \
    find / -iname PushThread.h && \
    mv /PushThread.h ./src/PushThread.h && \
    mv /hdbpp_es_Makefile ./Makefile && \
    make && \
    make install

# Install hdbpp-cm
RUN cd /hdb++ && \
    git clone https://github.com/tango-controls-hdbpp/hdbpp-cm.git && \
    cd hdbpp-cm && \
    find / -iname HdbConfigurationManager.h && \
    mv /HdbConfigurationManager.h ./src/HdbConfigurationManager.h && \
    mv /hdbpp_cm_Makefile ./Makefile && \
    make && \
    make install

RUN find / -iname mysql.h

# Install libhdbpp-mysql
#RUN cd /hdb++ && \
#    git clone https://github.com/tango-controls-hdbpp/libhdbpp-mysql.git && \
#    cd libhdbpp-mysql && \
#    mv /LibHdb++MySQL.h ./src/LibHdb++MySQL.h && \
#    mv /libhdbpp-mysql_Makefile ./Makefile && \
#    make
#RUN make install

# Install libhdbpp-cassandra
RUN cd /hdb++ && \
    git clone http://github.com/tango-controls-hdbpp/libhdbpp-cassandra.git && \
    cd libhdbpp-cassandra && \
    find / -iname LibHdb++Cassandra.h && \
    mv /LibHdb++Cassandra.h ./src/LibHdb++Cassandra.h && \
    mkdir build && \
    cd build && \
    ls /hdb++/libhdbpp-cassandra && \
    find / -iname libhdbppcassandra.so && \
    ls /hdb++/libhdbpp-cassandra/build && \
    cmake -DCMAKE_INSTALL_PREFIX="/hdb++/libhdbpp-cassandra" -DCMAKE_INCLUDE_PATH="/usr/local/include/tango;/hdb++/libhdbpp/src" -DCMAKE_LIBRARY_PATH="/usr/local/lib" .. && \
    make && \
    make install

ENV LD_LIBRARY_PATH="/hdb++/libhdbpp/lib:/hdb++/libhdbpp-cassandra/build"
ENV TANGO_HOST=localhost:10000
RUN cd /hdb++/hdbpp-es/bin && \
    find / -iname libhdb++.so.6 && \
    echo $TANGO_HOST

ENTRYPOINT "HdbEventSubscriber" "01"