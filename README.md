# ロボットシステム学課題2
---

動作環境
---
Ubuntu 20.04 server

ROS noetic

---

使用したもの
---
Raspberry Pi 4

---

概要
---
演算子と2つの整数を入力すると計算します。

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

1.
```
   $ roscore
   ```
   
2.publisher
 ```
   $ rosrun mypkg input.py
   ```

3.subscriber
 ```
   $ rosrun mypkg result.py
   ```
   
publisherの端末に演算子、数字を入力するとsubscriberに答えが出力されます。

動画
---


---

ライセンス
---
[GNU General Public License v3.0](https://github.com/uvershuta/RobotSystem1/blob/main/COPYING)
