#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import jpype

jvm_path = "/usr/lib/jvm/java-8-oracle/jre/lib/amd64/server/libjvm.so"

jpype.startJVM(jvm_path, "-ea", "-Djava.class.path=/home/acaliskan/github/python-zemberek/zemberek-morphology-0.9.3.jar")

morph_cls = jpype.JClass("zemberek/morphology/analysis/tr/TurkishMorphology")
