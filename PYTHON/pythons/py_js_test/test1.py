import execjs
print(execjs.get().name)


# eval()
# js_one = 'a = 12'
# print(execjs.eval(js_one))


# 代码多  使用compile()
with open('test1.js','r',encoding='utf-8') as f:
    data = f.read()

ctx = execjs.compile(data)
a = '123456'
result = ctx.call('a',a)
print(result)
