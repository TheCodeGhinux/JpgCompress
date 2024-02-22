import unittest
import os
from compress import load_image, flatten_image, compress_image, save_image

class TestImageCompression(unittest.TestCase):
    def setUp(self):
        self.input_image_path = "test_input.jpg"
        self.output_image_path = "test_output.jpg"
        self.image = load_image(self.input_image_path)
        self.flattened_image = flatten_image(self.image)

    def tearDown(self):
        if os.path.exists(self.output_image_path):
            os.remove(self.output_image_path)

    def test_load_image(self):
        self.assertIsNotNone(self.image)

    def test_flatten_image(self):
        self.assertEqual(self.flattened_image.shape[1], 3)

    def test_compress_image(self):
        compressed_image, _ = compress_image(self.flattened_image)
        self.assertEqual(compressed_image.shape, self.image.shape)

    def test_save_image(self):
        save_image(self.image, self.output_image_path)
        self.assertTrue(os.path.exists(self.output_image_path))

if __name__ == "__main__":
    unittest.main()
