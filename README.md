# 安装

## 依赖
本代码库需要python3.x运行环境，使用前先安装依赖库：
```
pip3 install -r requirements.txt
```

## 爱小童SDK
```
pip3 install .
```

# 调用示例

将<AK_ID>和<AK_SECRET>替换成开发者的akId和akSecret。

```python3
from aixiaotong.face.face_compare_client import FaceCompareClient

if __name__ == '__main__':
    def test_path(*args, **kwargs):
        try:
            print(FaceCompareClient('<AK_ID>', '<AK_SECRET>').compare('data/000.jpg', 'data/001.jpg'))
        except Exception as e:
            print(e)

    # Single
    test_path()

    # Batch
    from multiprocessing.dummy import Pool
    pool = Pool(2)
    pool.map(test_path, range(10))
```