# 静力分析结果云图绘制和数据提取
1. 节点荷载
    1. GUI操作
    >List Result-Nodal Loads
    2. APDL
    
2. 支座反力
    1. GUI操作
    >List Result-Reaction Solu
    2.  APDL
    
3. 结构变形
    1. GUI操作
    >Plot Result-Deformed Shape
    
    or
    
    >Plot Result-Contour Plot-Nodal Solu-Nodal Solution-DOF Solution-Y Component of displacement

    2.APDL
      1. 绘制云图
      ```
      plnsol,u,y
      ```
      2. 提取结果
      
4. 结构应力（应变）
    1. GUI操作
    >Plot Result-Contour Plot-Nodal Solu-Nodal Solution-Stress
    2.  APDL
    
5. 结构轴向力和轴向应力
    1.APDL
    ```
    Etable,ZL,smisc,1!轴向力
    Pletable,ZL
    ```
    ```
    Etable,ZYL,smisc,31!轴向应力
    Pletable,ZYL
    ```
6. 绘制弯矩图
    1. APDL
    ```
    Etable,WJ1,smisc,2
    Etable,WJ2,smisc,15
    Plls,WJ1,WJ2
    ```
8. 绘制结果数值
    >PlotCtrls-Numbering Controls-SVAL On
