FROM nexus.engageska-portugal.pt/ska-docker/tango-java:latest

RUN apt update \
 && apt install -y \
    checkinstall \
    curl \

RUN mkdir hdbpp_viewer \
 && curl -o ATKCore.jar ftp://ftp.esrf.eu/pub/cs/tango/Atk/ATKCore.jar \
 && curl -o ATKWidget.jar ftp://ftp.esrf.eu/pub/cs/tango/Atk/ATKWidget.jar \
 && curl -o HDB++.jar https://bintray.com/tango-controls/maven/libhdbpp-java/1.25?pkgPath=%2Ftango-controls%2Fmaven%2Flibhdbpp-java#files/org%2Ftango%2Flibhdbpp-java%2F1.25 \
 && curl -o jcalendar.jar ftp://ftp.esrf.eu/pub/cs/tango/hdbviewer/jcalendar.jar \
 && curl -o jython.jar ftp://ftp.esrf.eu/pub/cs/tango/hdbviewer/jython.jar \
 && curl -o jhdbviewer.jar ftp://ftp.esrf.eu/pub/cs/tango/hdbviewer/jhdbviewer.jar \
 && curl -o JTango-9.0.3.jar https://sourceforge.net/projects/tango-cs/files/JTango/JTango-9.0.3/JTango-9.0.3.jar/download

ENV TANGO="/hdbpp_viewer/JTango-9.0.3.jar"
ENV TANGOATK="/hdbpp_viewer/ATKCore.jar:/hdbpp_viewer/ATKWidget.jar"
ENV HDBVIEWER="/hdbpp_viewer/jhdbviewer.jar"
ENV HDBPP="/hdbpp_viewer/HDB++.jar"
ENV JYTHON="/hdbpp_viewer/jython.jar"
ENV JCALENDAR="/hdbpp_viewer/jcalendar.jar"
ENV CLASSPATH=$CLASSPATH:$TANGO:$TANGOATK:$HDBPP:$JYTHON:$JCALENDAR:$HDBVIEWER

RUN echo $CLASSPATH