from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('/home/kunal/work/ksaluja15.github.io/img/svd_tiger.png')
img = np.array(img)
gray = 0.2989 * img[:, :, 0] + 0.5870 * img[:, :, 1] + 0.1140 * img[:, :, 2]

U,s,V = np.linalg.svd(gray)

recon_imgs=[]
for n in [5, 15, 30]:
    S = np.zeros(np.shape(gray))
    for i in range(0, n):
        S[i,i] = s[i]

    recon_img = U @ S @ V
    recon_imgs.append(recon_img)


fig, ax = plt.subplots(2, 2)

ax[0][0].imshow(gray, cmap='gray')
ax[0][0].axis('off')
ax[0][0].set_title('Original')

ax[0][1].imshow(recon_imgs[0], cmap='gray')
ax[0][1].axis('off')
ax[0][1].set_title(f'Reconstructed n = 5')

ax[1][0].imshow(recon_imgs[1], cmap='gray')
ax[1][0].axis('off')
ax[1][0].set_title(f'Reconstructed n = 15')

ax[1][1].imshow(recon_imgs[2], cmap='gray')
ax[1][1].axis('off')
ax[1][1].set_title(f'Reconstructed n = 30')
plt.show()