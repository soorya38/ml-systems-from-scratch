import unittest

from tensor.utils import infer_shape, numel, infer_dtype, flatten

class TestTensorUtils(unittest.TestCase):
    def test_infer_shape(self):
        self.assertEqual(infer_shape([1, 2, 3]), (3, ))
        self.assertEqual(infer_shape([[1, 2, 3], [4, 5, 6]]), (2, 3))
        self.assertEqual(infer_shape([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]), (2, 2, 3))
        self.assertEqual(infer_shape([]), (0, ))
        # Ragged/inconsistent nesting must raise, not silently return a shape
        with self.assertRaises(ValueError):
            infer_shape([1, [2, 3], [4, [5, 6]]])

    def test_numel(self):
        self.assertEqual(numel([1, 2, 3]), 3)
        self.assertEqual(numel([[1, 2, 3], [4, 5, 6]]), 6)
        self.assertEqual(numel([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]), 12)
        self.assertEqual(numel([]), 0)
        with self.assertRaises(ValueError):
            numel([1, [2, 3], [4, [5, 6]]])

    def test_infer_dtype(self):
        self.assertEqual(infer_dtype([1, 2, 3]), int)
        self.assertEqual(infer_dtype([[1, 2, 3], [4, 5, 6]]), int)
        self.assertEqual(infer_dtype([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]), int)
        with self.assertRaises(ValueError):
            infer_dtype([])
        self.assertEqual(infer_dtype([1, [2, 3], [4, [5, 6]]]), int)

    def test_flatten(self):
        self.assertEqual(flatten([1, 2, 3]), [1, 2, 3])
        self.assertEqual(flatten([[1, 2, 3], [4, 5, 6]]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(flatten([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(flatten([]), [])
        self.assertEqual(flatten([1, [2, 3], [4, [5, 6]]]), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()