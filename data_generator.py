# for i in range(100) 会生成一个容量为100的列表
# for i in xrange(100) 不会生成容量为100的列表，每次都返回一个值，只占用一个内存空间
# 同理 yield 用于把一个函数变成一个generator
# 调用__next__()方法可以看到输出值
class data_generator:
    def __init__(self, data, label, batch_size=8, shuffle=True):
        self.data = data
        self.label = label
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.steps = len(self.data) // self.batch_size
        if len(self.data) % self.batch_size != 0:
            self.steps += 1
    def __len__(self):
        return self.steps
    def __iter__(self):
        while True:
            idxs = list(range(len(self.data)))
            
            if self.shuffle:
                np.random.shuffle(idxs)
            
            X, Y = [], []
            for i in idxs:
                x = self.data[i]
                y = self.label[i]
                X.append(x)
                Y.append(y)
                if len(X) == self.batch_size or i == idxs[-1]:
                    yield np.array(X), np.array(Y)
                    X, Y = [], []
                    
                    
train = data_generator(data, label, BATCH_SIZE, True)
train.__iter__().__next__()
