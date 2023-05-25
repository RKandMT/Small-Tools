# 配置APDL运行环境
1. 运行程序ANSYS Mechanical APDL Product Launcher；
2. 在File Management选显卡中填写工作空间和文件名称；
3. 点击Run运行。
# 设置并行高性能运算
并行分析可以调用更多CPU，加快运行速度；**此操作还可以解决位移云图不显示的问题。**
1. 运行程序ANSYS Mechanical APDL Product Launcher；
2. 在High Performance Computing Setup选项卡中选择Use Shared-Memory Parallel(SMP)；
3. Number of Processors按实际情况选择（例如电脑的CPU是八核，则该数字应大于等于2，小于等于8）。
