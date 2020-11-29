# from modules.test import *
from modules.imagepreprocessor import *


# asd = imagepreprocessor()


#path = "C:\\Users\\Prashant\\Documents\\SudokuSolver\\
path = "dataset\\sudoku\\original\\image1013.original.jpg"
l = imagepreprocessor(path)
print("hi")
out = l.extractSudoku()
print(out)
cv2.imshow("as",out)
cv2.waitKey(0)
cv2.destroyAllWindows()


# asd = test
# u = modules.test()
# print("hi")