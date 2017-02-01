#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import jpype

# JVM / JAR Info
jvm_path = jpype.get_default_jvm_path()
jar_file = "zemberek-all-0.10.0.jar"

# Start JVM
jpype.startJVM(jvm_path, "-Djava.class.path="+jar_file, "-ea")



# Stop JVM
jpype.shutdownJVM()
