# ロボットシステム学課題2
---

動作環境
---
Ubuntu 20.04 server

---

概要
---


---


インストール方法
---

```
   $ cd catkin_ws/src
   $ git clone https://github.com/uvershuta/Robosys2.git
   $ cd ..
   $ catkin_make
   $ source ~/.bashrc
   ```
   
実行方法
---

```
   $ cd catkin_ws/src/mypkg/scripts
   $ chmod +x input.py
   $ chmod +x result.py
   ```

次に端末を3つ開きそれぞれで次のコマンドを打つ。

1つ目
```
   $ roscore
   ```
   
 ```
   $ rosrun mypkg input.py
   ```
   
 ```
   $ rosrun mypkg result.py
   ```

動画
---
https://youtu.be/l9GRMsLbqrM

---

ライセンス
---
[GNU General Public License v3.0](https://github.com/uvershuta/RobotSystem1/blob/main/COPYING)
