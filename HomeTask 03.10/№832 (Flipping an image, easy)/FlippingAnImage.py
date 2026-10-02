class Solution(object):
    def flipAndInvertImage(self, image):
        n = len(image)
        for i in range(n):
            for j in range(((n - 1) // 2) + 1):
                if image[i][j] == image[i][n - 1 - j]:
                    image[i][j] = 1 - image[i][j]
                    if n % 2 == 0 or j != (n - 1) // 2:
                        image[i][n - 1 - j] = 1 - image[i][n - 1 - j]
        return image