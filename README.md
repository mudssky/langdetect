# langdetect
检测中文,英语,韩文,日文,4种语言的文本

利用不同语言的unicode字符区间不同来进行检测.
因为中日韩使用了相同的汉字,所以区分不一定准确
对每个字符使用正则判断,按匹配的字符数目,判断各种语言字符的占比,占比最高的那个语言就是结果
匹配不到的字符串按照默认语言处理,或者当成未知语言
