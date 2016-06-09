# numpy, opencv, and xlwt python packages required
import numpy as np
import cv2
import math 
import xlwt

Patch = cv2.imread('patch.jpg', 0)      #edit the file name
Patch = Patch.tolist()
x = len(Patch)
y = len(Patch[0])

x = x/2
y = y/2
a = x-16
b = y-16

I2 = [[0.0]*32 for i in range(32)]

#selecting patch of size 32*32 pixels right in the middle
for i in range(32):
	for j in range(32):
		I2[i][j] = Patch[a][b]
		a = a+1
	a = x-16
	b = b+1
#cv2.imwrite('modified.jpg', np.array(I2))      #uncomment incase you want to write the patch as a new image

Patch_scaled = I2
for i in range(0, 32):
    for j in range(0, 32):
	Patch_scaled[i][j] = int(math.floor(Patch_scaled[i][j]*32.0/255.0))     #to get pixel values from 0 to 32
                                                                                #to normalize, replace 32 by 1, ie, divide by 32

Glcm = [[0]*32 for i in range(32)]
for i in range(0, 32):
    for j in range(0, 31):
        Glcm[Patch_scaled[i][j]][Patch_scaled[i][j+1]] = Glcm[Patch_scaled[i][j]][Patch_scaled[i][j+1]] + 1

#to create transpose of GLCM matrix
Glcm_transpose = (np.array(Glcm).transpose()).tolist()

#adding glcm matrix with its transpose to get probability density
Glcm_symm = [[0.0]*32 for i in range(32)]
for i in range(len(Glcm)):  
   for j in range(len(Glcm[0])):
        Glcm_symm[i][j] = float(Glcm[i][j]) + float(Glcm_transpose[i][j])

sum = 0.0
for i in range(len(Glcm)):  
   for j in range(len(Glcm[0])):
        sum = sum + Glcm_symm[i][j]
		
Glcm_probdist = [[0.0]*32 for i in range(32)]
for i in range(32):  
   for j in range(32):		
	    Glcm_probdist[i][j] = Glcm_symm[i][j]/sum

### Feature calculations		
contrast = 0
for i in range(0, 32):
    for j in range(0, 32):
        contrast = contrast + Glcm_probdist[i][j]*((i-j)**2)

dissimilarity = 0
for i in range(0, 32):
    for j in range(0, 32):
        dissimilarity = dissimilarity + Glcm_probdist[i][j]*abs(i-j)

homogeneity = 0
for i in range(0, 32):
    for j in range(0, 32):
        homogeneity = homogeneity + Glcm_probdist[i][j]/(1 + (i-j)**2)

ASM = 0
for i in range(0, 32):
    for j in range(0, 32):
        ASM = ASM + Glcm_probdist[i][j]**2

entropy = 0
for i in range(0, 32):
    for j in range(0, 32):
        if Glcm_probdist[i][j] != 0:
            entropy = entropy - Glcm_probdist[i][j]*math.log10(Glcm_probdist[i][j])

GLCM_mean_i = 0
GLCM_mean_j = 0
for i in range(0, 32):
    for j in range(0, 32):
        GLCM_mean_i = GLCM_mean_i + (i)*Glcm_probdist[i][j]

for i in range(0, 32):
    for j in range(0, 32):
        GLCM_mean_j = GLCM_mean_j + (j)*Glcm_probdist[i][j]

GLCM_variance_i = 0
for i in range(0, 32):
    for j in range(0, 32):
        GLCM_variance_i = GLCM_variance_i + Glcm_probdist[i][j]*((i-GLCM_mean_i)**2)
		
GLCM_variance_j = 0
for i in range(0, 32):
    for j in range(0, 32):
        GLCM_variance_j = GLCM_variance_j + Glcm_probdist[i][j]*((j-GLCM_mean_j)**2)
		
GLCM_correlation = 0
for i in range(0, 32):
    for j in range(0, 32):
        GLCM_correlation = GLCM_correlation + Glcm_probdist[i][j]*(i-GLCM_mean_i)*(j-GLCM_mean_j)/math.sqrt(GLCM_variance_i*GLCM_variance_j)
		
#exporting the features to an excel sheet		
style0 = xlwt.easyxf('font: name Times New Roman, color-index black, bold on',num_format_str='#,##0.00')
wb = xlwt.Workbook()
ws = wb.add_sheet('Features')
ws.write(0, 0, 'contrast', style0)
ws.write(0, 1, 'dissimilarity', style0)
ws.write(0, 2, 'homogeneity', style0)
ws.write(0, 3, 'ASM', style0)
ws.write(0, 4, 'entropy', style0)
ws.write(0, 5, 'GLCM_mean_i', style0)
ws.write(0, 6, 'GLCM_variance_i', style0)
ws.write(0, 7, 'GLCM_correlation', style0)
ws.write(1, 0, contrast)
ws.write(1, 1, dissimilarity)
ws.write(1, 2, homogeneity)
ws.write(1, 3, ASM)
ws.write(1, 4, entropy)
ws.write(1, 5, GLCM_mean_i)
ws.write(1, 6, GLCM_variance_i)
ws.write(1, 7, GLCM_correlation)
wb.save('features.xls')
