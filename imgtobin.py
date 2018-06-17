import numpy as np


def slice_img(img):
    n, ch, x, y = img.shape
    out_shape = (8, x, y)
    out = np.zeros((n, 24, x, y))
    for i in range(n):
        out1 = np.unpackbits(img[i][0].reshape(x * y, 1), axis=1).T.reshape(out_shape)
        out2 = np.unpackbits(img[i][1].reshape(x * y, 1), axis=1).T.reshape(out_shape)
        out3 = np.unpackbits(img[i][2].reshape(x * y, 1), axis=1).T.reshape(out_shape)
        per_img = np.concatenate([out1, out2, out3])
        # import pdb
        # pdb.set_trace()
        out[i] = per_img
        # out = np.append(out, per_img, axis=0)

    return out

# if __name__ == "__main__":
#     a = np.arange(12).reshape(3, 2, 2).astype('uint8')
#     print('Input size = ', a.shape)
#     print('Input array = ')
#     print(a)

#     b = slice_img(a)
#     print('Output size = ', b.shape)
#     print('Output array = ')
#     print(b)
