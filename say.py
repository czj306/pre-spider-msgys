# -*- coding: utf-8 -*-

import pyttsx3


with open("./《美食供应商》最新章节列表/第一千一百零五章 尊师重道.txt") as f:
  engine = pyttsx3.init() # object creation
  msg = f.read()

  engine.say(msg)
  engine.runAndWait()
  engine.stop()