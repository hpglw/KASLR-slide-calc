# KASLR-slide-calc
用于计算黑苹果KASLR slide值的python脚本

首先，我不怎么会写python的，这个自己用的，运行过没什么问题，但还是会有些缺陷。
这两个py脚本主要一是自动计算slide值，并列出来。二是自动转换MMIO值为10进制，可以直接填入config.plist里面。

这个工具是根据这个教程弄的，主要是方便计算：
[Fixing KASLR slide values](https://dortania.github.io/OpenCore-Install-Guide/extras/kaslr-fix.html#fixing-kaslr-slide-values)

使用方法：
1. 按上面的教程，得到memmap.txt
2. 将此文件放在脚本同一目录
3. 分别运行两个脚本即可生成一个为MMIO.txt和一个slide=.txt文件

## 特别注意！slide=.txt里面的值，要加1的，这个自己加，如里面是11的，最终slide值就是12.如出现多个0的值，那么slide值不是0就是1两个都试一下。slide值不会大于256.

## MMIO值适用于DevirtualiseMmio方法
