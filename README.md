# simple-gcc-stm32-project

gdb调试代码使用工程，代码中含有dwt和itm寄存器的配置

完成了itm_print功能，以及dwt_cyccnt功能

itm_print需要配合openocd的itmdump工具使用

而dwt_cyccnt为了使得对原有代码的影响达到最小，在openocd中进行读取寄存器以及复位寄存器操作

工程目前已经稳定  by 20180127
