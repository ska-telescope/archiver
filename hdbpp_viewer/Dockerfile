FROM nexus.engageska-portugal.pt/ska-docker/tango-java:latest
USER root
RUN apt-get update
RUN apt-get install -y --force-yes curl

#RUN mkdir hdbpp_viewer \
WORKDIR hdbpp_viewer
RUN curl -o ATKCore.jar ftp://ftp.esrf.eu/pub/cs/tango/Atk/ATKCore.jar \
 && curl -o ATKWidget.jar ftp://ftp.esrf.eu/pub/cs/tango/Atk/ATKWidget.jar \
 && curl -o HDB++.jar https://bintray.com/tango-controls/maven/libhdbpp-java/1.25?pkgPath=%2Ftango-controls%2Fmaven%2Flibhdbpp-java#files/org%2Ftango%2Flibhdbpp-java%2F1.25 \
 && curl -o jcalendar.jar ftp://ftp.esrf.eu/pub/cs/tango/hdbviewer/jcalendar.jar \
 && curl -o jython.jar ftp://ftp.esrf.eu/pub/cs/tango/hdbviewer/jython.jar \
 && curl -o jhdbviewer.jar ftp://ftp.esrf.eu/pub/cs/tango/hdbviewer/jhdbviewer.jar \
 && curl -o JTango.jar https://sourceforge.net/projects/tango-cs/files/JTango/JTango-9.0.3/JTango-9.0.3.jar/download \
 && ls

ENV TANGO="hdbpp_viewer/JTango.jar"
ENV TANGOATK="hdbpp_viewer/ATKCore.jar:hdbpp_viewer/ATKWidget.jar"
ENV HDBVIEWER="hdbpp_viewer/jhdbviewer.jar"
ENV HDBPP="hdbpp_viewer/HDB++.jar"
ENV JYTHON="hdbpp_viewer/jython.jar"
ENV JCALENDAR="hdbpp_viewer/jcalendar.jar"

RUN find . -iname JTango.jar
RUN find . -iname ATKCore.jar
RUN find . -iname ATKWidget.jar
RUN find . -iname jhdbviewer.jar
RUN find . -iname HDB++.jar
RUN find . -iname jython.jar
RUN find . -iname jcalendar.jar
RUN find . -iname java
RUN echo $CLASSPATH

ENV HDB_TYPE=mysql
ENV HDB_MYSQL_HOST=archiver-maria-db
ENV HDB_USER="tango"
ENV HDB_PASSWORD="tango"
ENV HDB_NAME=hdbpp

ENV CLASSPATH=$CLASSPATH:$TANGO:$TANGOATK:$HDBPP:$JYTHON:$JCALENDAR:$HDBVIEWER
#ENV CLASSPATH=hdbpp_viewer/jhdbviewer.jar
RUN echo $CLASSPATH
RUN find . -name "*.jar" | xargs grep HDBViewer.MainPanel
#RUN find *.jar | xargs grep MainPanel.class
#ENTRYPOINT ["/bin/bash", "-c", "java -Djava.util.logging.config.file=log.properties -DTANGO_HOST=$TANGO_HOST HDBViewer.MainPanel $@"]
#ENTRYPOINT ["/usr/bin/java", "-Djava.util.logging.config.file=log.properties","-DTANGO_HOST=$TANGO_HOST","HDBViewer.MainPanel"]
CMD java -Djava.util.logging.config.file=log.properties -DTANGO_HOST=$TANGO_HOST HDBViewer.MainPanel $@
#CMD ["java","-classpath", "/hdbpp_viewer/JTango-9.0.3.jar;/hdbpp_viewer/ATKCore.jar:/hdbpp_viewer/ATKWidget.jar;/hdbpp_viewer/jhdbviewer.jar;/hdbpp_viewer/jhdbviewer.jar;/hdbpp_viewer/HDB++.jar;/hdbpp_viewer/jython.jar;/hdbpp_viewer/jcalendar.jar","-Djava.util.logging.config.file=log.properties","-DTANGO_HOST=$TANGO_HOST","HDBViewer.MainPanel"]
#RUN java -cp /hdbpp_viewer/jhdbviewer.jar HDBViewer.MainPanel


