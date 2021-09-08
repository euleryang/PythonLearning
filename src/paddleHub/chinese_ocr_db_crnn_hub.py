import paddlehub as hub
import cv2

ocr = hub.Module(name="chinese_ocr_db_crnn_server")
result = ocr.recognize_text(images=[cv2.imread('d:/words.jpg')])

# or
# result = ocr.recognize_text(paths=['/PATH/TO/IMAGE'])
# 打印预测结果
print(result)