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