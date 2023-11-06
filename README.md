# KASLR-slide-calc
用于计算黑苹果KASLR slide值的python脚本

首先，我不怎么会写python的，这个自己用的，运行过没什么问题，但还是会有些缺陷。
这两个py脚本主要一是自动计算slide值，并列出来。二是自动转换MMIO值为10进制，可以直接填入config.plist里面。

这个工具是根据这个教程弄的，主要是方便计算：
[Fixing KASLR slide values](https://dortania.github.io/OpenCore-Install-Guide/extras/kaslr-fix.html#fixing-kaslr-slide-values)

