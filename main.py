#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import jpype

# JVM / JAR Info
jvm_path = "/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server/libjvm.so"

# Start JVM
jpype.startJVM(jvm_path, "-ea", "-Djava.class.path=/home/acaliskan/github/python-zemberek/zemberek-tum-2.0.jar")

Tr = jpype.JClass("net.zemberek.tr.yapi.TurkiyeTurkcesi")
Zemberek = jpype.JClass("net.zemberek.erisim.Zemberek")

tr = Tr()
zemberek = Zemberek(tr)

yanit = zemberek.kelimeCozumle("futbolcularımız")
print(yanit[a])

# Stop JVM
jpype.shutdownJVM()
